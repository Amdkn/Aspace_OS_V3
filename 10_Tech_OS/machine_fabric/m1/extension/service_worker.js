const HOST = "com.aspace.machine_fabric.canary";
const OPERATION_ID = "m1-browser-op-0001";
const ACTION = {action:"set_text", selector:"#target", value:"AFTER"};

let nativePort = null;
let reconnectTimer = null;
let backoff = 1000;
let isCanaryRunning = false;

async function sha256(text) {
  const bytes = new TextEncoder().encode(text);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return [...new Uint8Array(digest)].map(b=>b.toString(16).padStart(2,"0")).join("");
}

function connect() {
  if (nativePort) return;
  console.log("Connecting to native host:", HOST);

  try {
    nativePort = chrome.runtime.connectNative(HOST);
  } catch (e) {
    console.error("Failed to connect:", e);
    scheduleReconnect();
    return;
  }

  backoff = 1000;

  nativePort.onMessage.addListener(async (msg) => {
    if (msg && msg.execute && msg.action === "browser.dom.action") {
        try {
            const {tabs, tab} = await findCanaryTab();
            if (tab && tab.id) {
                const results = await chrome.scripting.executeScript({
                  target:{tabId:tab.id},
                  func:(selector,value)=>{
                    const el=document.querySelector(selector);
                    if(!el) return {ok:false,error:"selector_not_found",selector};
                    const before=el.textContent;
                    el.textContent=value;
                    return {ok:true,selector,before,after:el.textContent,url:location.href};
                  },
                  args:[msg.selector || ACTION.selector, msg.value || ACTION.value]
                });
                const evidence = results && results[0] ? results[0].result : {ok:false,error:"no_result"};
                const fingerprint = await sha256(JSON.stringify(ACTION));
                nativePort.postMessage({
                    type: "complete",
                    operation_id: msg.operation_id || OPERATION_ID,
                    fingerprint: msg.fingerprint || fingerprint,
                    evidence: evidence
                });
            }
        } catch(e) {
            console.error(e);
        }
    }
  });

  nativePort.onDisconnect.addListener(() => {
    let err = chrome.runtime.lastError;
    console.error("Native host disconnected:", err ? err.message : "unknown");
    nativePort = null;
    scheduleReconnect();
  });

  // Try canary after connecting
  runCanary();
}

function scheduleReconnect() {
  clearTimeout(reconnectTimer);
  console.log("Scheduling reconnect in", backoff, "ms");
  reconnectTimer = setTimeout(() => {
    connect();
  }, backoff);
  backoff = Math.min(backoff * 2, 60000);
}

async function findCanaryTab() {
  const tabs = await chrome.tabs.query({});
  let tab = tabs.find(t => (t.url || "").includes("/canary.html"));
  return {tabs, tab};
}

async function runCanary() {
    if (!nativePort || isCanaryRunning) return;
    isCanaryRunning = true;
    try {
        let {tabs, tab} = await findCanaryTab();
        nativePort.postMessage({type:"hello"});
        nativePort.postMessage({type:"tabs", tabs:tabs.map(t=>({id:t.id,url:t.url,title:t.title,active:t.active}))});
        if (tab && tab.id) {
            const fingerprint = await sha256(JSON.stringify(ACTION));
            nativePort.postMessage({type:"claim", operation_id:OPERATION_ID, fingerprint, action:"browser.dom.action", selector:ACTION.selector, value:ACTION.value});
        }
    } catch(e) {
        console.error("Canary error", e);
    } finally {
        isCanaryRunning = false;
    }
}

chrome.runtime.onMessage.addListener((msg)=>{
  if (msg && msg.type === "kick") setTimeout(runCanary,50);
});

chrome.runtime.onInstalled.addListener(() => {
  connect();
});

chrome.runtime.onStartup.addListener(() => {
  connect();
});

chrome.tabs.onUpdated.addListener((tabId,change,tab)=>{
  if ((tab.url || change.url || "").includes("/canary.html") && change.status === "complete") {
      setTimeout(runCanary, 250);
  }
});

// Always connect on script wake
connect();
