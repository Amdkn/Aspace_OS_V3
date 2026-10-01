const HOST = "com.aspace.machine_fabric.m1";
let port = null;

async function sha256(text) {
  const bytes = new TextEncoder().encode(text);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return [...new Uint8Array(digest)].map(b=>b.toString(16).padStart(2,"0")).join("");
}

function nativeRequest(msg) {
  return new Promise((resolve, reject) => {
    if (!port) return reject(new Error("no port"));
    const requestId = crypto.randomUUID();
    const timer = setTimeout(()=>reject(new Error("native timeout")), 5000);
    const listener = response => {
      clearTimeout(timer);
      port.onMessage.removeListener(listener);
      resolve(response);
    };
    port.onMessage.addListener(listener);
    port.postMessage({...msg, request_id:requestId});
  });
}

async function runTask(taskMsg) {
  try {
    const fingerprint = await sha256(JSON.stringify(taskMsg));
    
    let selector = taskMsg.selector;
    let value = taskMsg.value;
    
    // Support nested gateway payload format
    if (taskMsg.payload) {
      if (taskMsg.payload.selector) selector = taskMsg.payload.selector;
      if (taskMsg.payload.value) value = taskMsg.payload.value;
    }

    const claim = await nativeRequest({
       type: "claim",
       operation_id: taskMsg.operation_id,
       fingerprint,
       action: "browser.dom.action",
       selector: selector,
       value: value
    });

    if (claim && claim.execute) {
      let evidence = {ok: false, error: "no_result"};
      let tabId = taskMsg.tab_id;
      if (!tabId) {
        // Try to find the active tab as a fallback
        const tabs = await chrome.tabs.query({active: true, currentWindow: true});
        if (tabs && tabs.length > 0) tabId = tabs[0].id;
      }

      if (tabId) {
        const results = await chrome.scripting.executeScript({
          target: {tabId: tabId},
          func: (sel, val) => {
            const el = document.querySelector(sel);
            if(!el) return {ok: false, error: "selector_not_found", selector: sel};
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
      await nativeRequest({type: "complete", operation_id: taskMsg.operation_id, fingerprint, evidence});
    }
  } catch(e) {
    console.error(e);
  }
}

function connect() {
  if (port) return;
  port = chrome.runtime.connectNative(HOST);
  port.onMessage.addListener(async (msg) => {
     if (msg && msg.action === "browser.dom.action") {
       await runTask(msg);
     }
  });
  port.onDisconnect.addListener(() => {
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
           runTask(task);
        }
      }
      const tabs = await chrome.tabs.query({});
      await nativeRequest({type: "tabs", tabs: tabs.map(t=>({id:t.id,url:t.url,title:t.title,active:t.active}))});
    } catch(e) { }
  }
  setTimeout(pingLoop, 5000);
}

chrome.runtime.onInstalled.addListener(() => { connect(); setTimeout(pingLoop, 1000); });
chrome.runtime.onStartup.addListener(() => { connect(); setTimeout(pingLoop, 1000); });
chrome.runtime.onMessage.addListener((msg) => {
  if (msg && msg.type === "kick") { connect(); }
});
connect();
setTimeout(pingLoop, 1000);
