try {
  chrome.runtime.sendMessage({type:"kick", url:location.href});
} catch (e) {
  document.documentElement.dataset.aspaceKickError=String(e);
}
