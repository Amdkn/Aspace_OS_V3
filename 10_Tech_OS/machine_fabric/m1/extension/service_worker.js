const HOST = "com.aspace.machine_fabric.m1";
let port = null;
const pendingRequests = new Map();
const activeTasks = new Set();

async function sha256(text) {
  const bytes = new TextEncoder().encode(text);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return [...new Uint8Array(digest)].map(b=>b.toString(16).padStart(2,"0")).join("");
}

function settleNativeResponse(msg) {
  const requestId = msg && msg.request_id;
  if (!requestId || !pendingRequests.has(requestId)) return false;
  const pending = pendingRequests.get(requestId);
  pendingRequests.delete(requestId);
  clearTimeout(pending.timer);
  pending.resolve(msg);
  return true;
}

function nativeRequest(msg) {
  return new Promise((resolve, reject) => {
    if (!port) return reject(new Error("no port"));
    const requestId = crypto.randomUUID();
    const timer = setTimeout(() => {
      pendingRequests.delete(requestId);
      reject(new Error("native timeout"));
    }, 5000);
    pendingRequests.set(requestId, {resolve, reject, timer});
    try {
      port.postMessage({...msg, request_id: requestId});
    } catch (e) {
      clearTimeout(timer);
      pendingRequests.delete(requestId);
      reject(e);
    }
  });
}

async function runTask(taskMsg) {
  const operationId = taskMsg && taskMsg.operation_id;
  if (!operationId || activeTasks.has(operationId)) return;
  activeTasks.add(operationId);

  let fingerprint = null;
  let claimed = false;
  try {
    fingerprint = taskMsg.fingerprint || await sha256(JSON.stringify(taskMsg));

    let selector = taskMsg.selector;
    let value = taskMsg.value;

    if (taskMsg.payload) {
      if (taskMsg.payload.selector) selector = taskMsg.payload.selector;
      if (taskMsg.payload.value !== undefined) value = taskMsg.payload.value;
    }

    const claim = await nativeRequest({
      type: "claim",
      operation_id: operationId,
      fingerprint,
      action: "browser.dom.action",
      selector,
      value
    });

    if (!claim || !claim.execute) return;
    claimed = true;

    let evidence = {ok: false, error: "no_result"};
    let tabId = taskMsg.tab_id;
    if (!tabId) {
      const tabs = await chrome.tabs.query({active: true, currentWindow: true});
      if (tabs && tabs.length > 0) tabId = tabs[0].id;
    }

    if (tabId) {
      const results = await chrome.scripting.executeScript({
        target: {tabId},
        func: (sel, val) => {
          const el = document.querySelector(sel);
          if (!el) return {ok: false, error: "selector_not_found", selector: sel, url: location.href};
          const before = el.textContent;
          if (val !== undefined) el.textContent = val;
          return {ok: true, selector: sel, before, after: el.textContent, url: location.href};
        },
        args: [selector, value]
      });
      if (results && results[0]) evidence = results[0].result;
    } else {
      evidence = {ok: false, error: "no_active_tab"};
    }

    await nativeRequest({
      type: "complete",
      operation_id: operationId,
      fingerprint,
      evidence
    });
  } catch (e) {
    console.error(e);
    if (claimed && fingerprint) {
      try {
        await nativeRequest({
          type: "complete",
          operation_id: operationId,
          fingerprint,
          evidence: {
            ok: false,
            error: "extension_exception",
            message: String(e && e.message ? e.message : e)
          }
        });
      } catch (completeError) {
        console.error(completeError);
      }
    }
  } finally {
    activeTasks.delete(operationId);
  }
}

function connect() {
  if (port) return;
  try {
    port = chrome.runtime.connectNative(HOST);
  } catch (e) {
    port = null;
    setTimeout(connect, 2000);
    return;
  }

  port.onMessage.addListener(async (msg) => {
    if (settleNativeResponse(msg)) return;
    if (msg && msg.action === "browser.dom.action") {
      await runTask(msg);
    }
  });

  port.onDisconnect.addListener(() => {
    for (const [requestId, pending] of pendingRequests.entries()) {
      clearTimeout(pending.timer);
      pending.reject(new Error("native disconnected"));
      pendingRequests.delete(requestId);
    }
    port = null;
    setTimeout(connect, 2000);
  });
}

async function pingLoop() {
  if (port) {
    try {
      const helloResp = await nativeRequest({type: "hello"});
      if (helloResp && helloResp.tasks && helloResp.tasks.length > 0) {
        for (const task of helloResp.tasks) {
          await runTask(task);
        }
      }
      const tabs = await chrome.tabs.query({});
      await nativeRequest({
        type: "tabs",
        tabs: tabs.map(t=>({id:t.id,url:t.url,title:t.title,active:t.active}))
      });
    } catch(e) {
      console.error(e);
    }
  }
  setTimeout(pingLoop, 5000);
}

chrome.runtime.onInstalled.addListener(() => { connect(); setTimeout(pingLoop, 1000); });
chrome.runtime.onStartup.addListener(() => { connect(); setTimeout(pingLoop, 1000); });
chrome.runtime.onMessage.addListener((msg) => {
  if (msg && msg.type === "kick") connect();
});

connect();
setTimeout(pingLoop, 1000);
