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
    const claim = await nativeRequest({
       type: "claim",
       operation_id: taskMsg.operation_id,
       fingerprint,
       action: "browser.dom.action",
       selector: taskMsg.selector,
       value: taskMsg.value
    });

    if (claim && claim.execute) {
      let evidence = {ok: false, error: "no_result"};
      if (taskMsg.tab_id) {
        const results = await chrome.scripting.executeScript({
          target: {tabId: taskMsg.tab_id},
          func: (selector, value) => {
            const el = document.querySelector(selector);
            if(!el) return {ok: false, error: "selector_not_found", selector};
            const before = el.textContent;
            el.textContent = value;
            return {ok: true, selector, before, after: el.textContent, url: location.href};
          },
          args: [taskMsg.selector, taskMsg.value]
        });
        if (results && results[0]) evidence = results[0].result;
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
      await nativeRequest({type: "hello"});
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
