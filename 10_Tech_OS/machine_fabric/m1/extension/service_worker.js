const HOST = "com.aspace.machine_fabric.canary";
const OPERATION_ID = "m1-browser-op-0001";
const ACTION = {action:"set_text", selector:"#target", value:"AFTER"};

async function sha256(text) {
  const bytes = new TextEncoder().encode(text);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return [...new Uint8Array(digest)].map(b=>b.toString(16).padStart(2,"0")).join("");
}

function nativeRequest(port, msg) {
  return new Promise((resolve, reject) => {
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

async function findCanaryTab() {
  const tabs = await chrome.tabs.query({});
  let tab = tabs.find(t => (t.url || "").includes("/canary.html"));
  return {tabs, tab};
}

async function runCanary() {
  const marker = await chrome.storage.local.get(["canary_running"]);
  if (marker.canary_running) return;
  await chrome.storage.local.set({canary_running:true});
  try {
    let {tabs, tab} = await findCanaryTab();
    if (!tab || !tab.id) return;
    let port = chrome.runtime.connectNative(HOST);
    await nativeRequest(port, {type:"hello"});
    await nativeRequest(port, {type:"tabs", tabs:tabs.map(t=>({id:t.id,url:t.url,title:t.title,active:t.active}))});
    const fingerprint = await sha256(JSON.stringify(ACTION));
    const claim = await nativeRequest(port, {type:"claim", operation_id:OPERATION_ID, fingerprint, action:"browser.dom.action", selector:ACTION.selector, value:ACTION.value});
    if (claim.execute) {
      const results = await chrome.scripting.executeScript({
        target:{tabId:tab.id},
        func:(selector,value)=>{
          const el=document.querySelector(selector);
          if(!el) return {ok:false,error:"selector_not_found",selector};
          const before=el.textContent;
          el.textContent=value;
          return {ok:true,selector,before,after:el.textContent,url:location.href};
        },
        args:[ACTION.selector,ACTION.value]
      });
      const evidence = results && results[0] ? results[0].result : {ok:false,error:"no_result"};
      await nativeRequest(port, {type:"complete", operation_id:OPERATION_ID, fingerprint, evidence});
    }
    port.disconnect();
    await new Promise(r=>setTimeout(r,350));
    port = chrome.runtime.connectNative(HOST);
    await nativeRequest(port, {type:"hello"});
    await nativeRequest(port, {type:"claim", operation_id:OPERATION_ID, fingerprint, action:"browser.dom.action", selector:ACTION.selector, value:ACTION.value});
    port.disconnect();
    await chrome.storage.local.set({canary_done:true});
  } catch (e) {
    await chrome.storage.local.set({canary_error:String(e)});
  } finally {
    await chrome.storage.local.set({canary_running:false});
  }
}

chrome.runtime.onMessage.addListener((msg)=>{
  if (msg && msg.type === "kick") setTimeout(runCanary,50);
});
chrome.runtime.onInstalled.addListener(()=>setTimeout(runCanary,500));
chrome.runtime.onStartup.addListener(()=>setTimeout(runCanary,500));
chrome.tabs.onUpdated.addListener((tabId,change,tab)=>{
  if ((tab.url || change.url || "").includes("/canary.html") && change.status === "complete") setTimeout(runCanary,250);
});
