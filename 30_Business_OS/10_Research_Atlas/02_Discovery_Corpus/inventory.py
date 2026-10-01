import subprocess
import json
import os

class CorpusInventory:
    """Base interface for Corpus inventory adapters."""
    def get_urls(self, source_config):
        raise NotImplementedError("Inventory adapters must implement get_urls")

class StaticListInventory(CorpusInventory):
    """Fallback static list inventory."""
    def get_urls(self, source_config):
        return source_config.get("urls", [])

class YTDLPPlaylistInventory(CorpusInventory):
    """yt-dlp adapter for dynamic channel/playlist enumeration."""
    def get_urls(self, source_config):
        url = source_config.get("url")
        if not url:
            print("[Inventory] Missing 'url' for ytdlp_playlist")
            return []

        print(f"[Inventory] Enumerating playlist via yt-dlp: {url}")
        cmd = [
            "yt-dlp",
            "--flat-playlist",
            "--dump-json",
            url
        ]
        urls = []
        try:
            # Depending on platform availability, timeout or fail gracefully
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            for line in res.stdout.strip().split('\n'):
                if not line: continue
                try:
                    entry = json.loads(line)
                    # For youtube, the URL might be constructed or directly available
                    # 'webpage_url' or 'url' is usually present.
                    video_url = entry.get("webpage_url") or entry.get("url")
                    if video_url:
                        urls.append(video_url)
                    elif entry.get("id"):
                        urls.append(f"https://www.youtube.com/watch?v={entry.get('id')}")
                except json.JSONDecodeError:
                    pass
        except subprocess.CalledProcessError as e:
            print(f"[Inventory] yt-dlp enumeration failed: {e}")
        except Exception as e:
            print(f"[Inventory] Unexpected error in yt-dlp enumeration: {e}")

        return urls

def resolve_inventory(manifest):
    """
    Parses manifest config and dispatches to the correct inventory adapter.
    """
    inventory_type = manifest.get("type", "static")

    if inventory_type == "ytdlp_playlist":
        adapter = YTDLPPlaylistInventory()
    else:
        adapter = StaticListInventory()

    return adapter.get_urls(manifest)
