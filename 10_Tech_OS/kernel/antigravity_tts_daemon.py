import os
import sys
import time
import json
import re
import glob
import asyncio
import threading
import subprocess
import edge_tts
import win32com.client

AUDIO_CACHE_DIR = os.path.join(os.environ.get("USERPROFILE", r"C:\Users\amado"), ".antigravity_voice_cache")
os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)

DEFAULT_VOICE = "fr-FR-DeniseNeural"  # Options: fr-FR-DeniseNeural, fr-FR-HenriNeural, fr-FR-EloiseNeural

def clean_text_for_speech(text: str) -> str:
    """Nettoie le texte markdown pour une lecture vocale fluide et naturelle."""
    if not text:
        return ""
    # Retirer les blocs de code volumineux ```...```
    text = re.sub(r'```[\s\S]*?```', ' [Bloc de code technique omis]. ', text)
    # Retirer le code inline
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Retirer les liens markdown [nom](url) -> nom
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Retirer les balises d'images
    text = re.sub(r'!\[[^\]]*\]\([^\)]+\)', '', text)
    # Nettoyer les titres markdown #
    text = re.sub(r'#{1,6}\s*', '', text)
    # Nettoyer les séparateurs de tableaux markdown |---|---|
    text = re.sub(r'\|[ -:]*\|[ -:|]*', '', text)
    text = re.sub(r'\|', ', ', text)
    # Nettoyer le gras et l'italique * ou _
    text = re.sub(r'[*_]{1,3}([^*_]+)[*_]{1,3}', r'\1', text)
    # Nettoyer les balises HTML
    text = re.sub(r'<[^>]+>', '', text)
    # Nettoyer les puces
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    # Retirer le footer répétitif de lecture manuelle (Lecteur Audio, Écoute manuelle...)
    text = re.sub(r'---\s*\n\s*\*?\*?Écoute manuelle[\s\S]*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\*?Écoute manuelle\s*:[\s\S]*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'🎧\s*\**Lecteur Audio[\s\S]*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Lecteur Audio de cette réponse[\s\S]*$', '', text, flags=re.IGNORECASE)
    text = re.sub(r'python\s+10_Tech_OS/kernel/antigravity_tts_daemon\.py\s+--replay[\s\S]*$', '', text, flags=re.IGNORECASE)
    # Normaliser les espaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

async def generate_tts(text: str, output_path: str, voice: str = DEFAULT_VOICE):
    """Génère l'audio MP3 via edge-tts."""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

TTS_LOCK_FILE = os.path.join(AUDIO_CACHE_DIR, "tts_playing.lock")

def acquire_tts_lock():
    """Acquiert le verrou global de parole pour empêcher toute superposition."""
    for _ in range(50):
        try:
            if os.path.exists(TTS_LOCK_FILE):
                # Vérifier si le verrou est orphelin (plus vieux de 30 secondes)
                mtime = os.path.getmtime(TTS_LOCK_FILE)
                if time.time() - mtime > 30:
                    try:
                        os.remove(TTS_LOCK_FILE)
                    except Exception:
                        pass
                else:
                    time.sleep(0.2)
                    continue
            with open(TTS_LOCK_FILE, "w", encoding="utf-8") as f:
                f.write(str(os.getpid()))
            return True
        except Exception:
            time.sleep(0.2)
    return False

def release_tts_lock():
    """Libère le verrou global de parole."""
    try:
        if os.path.exists(TTS_LOCK_FILE):
            os.remove(TTS_LOCK_FILE)
    except Exception:
        pass

def play_audio(file_path: str):
    """Joue l'audio via PowerShell PresentationCore MediaPlayer (fiable sur Windows)."""
    if not os.path.exists(file_path):
        return
    ps_cmd = (
        f"Add-Type -AssemblyName presentationCore; "
        f"$p = New-Object System.Windows.Media.MediaPlayer; "
        f"$p.Open([System.Uri]'{file_path}'); "
        f"$p.Play(); "
        f"while ($p.NaturalDuration.HasTimeSpan -eq $false -or $p.Position -lt $p.NaturalDuration.TimeSpan) {{ "
        f"  Start-Sleep -Milliseconds 250 "
        f"}}"
    )
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=True)
    except Exception as e:
        print(f"[Audio Error] {e}", file=sys.stderr)
        # Fallback SAPI
        try:
            speaker = win32com.client.Dispatch("SAPI.SpVoice")
            speaker.Speak("Audio de réponse disponible.")
        except Exception:
            pass

def speak(text: str, voice: str = DEFAULT_VOICE, auto_play: bool = True):
    """Synthèse et lecture vocale d'un texte protégée par verrou global anti-superposition.
    Exporte systématiquement vers latest_speech.mp3 pour relecture manuelle instantanée.
    """
    clean = clean_text_for_speech(text)
    if not clean or len(clean) < 2:
        return
    if not acquire_tts_lock():
        print("[TTS] Verrou occupé par une lecture en cours, passage ignoré.")
        return
    try:
        ts_name = f"speech_{int(time.time()*1000)}.mp3"
        audio_file = os.path.join(AUDIO_CACHE_DIR, ts_name)
        asyncio.run(generate_tts(clean, audio_file, voice))
        
        # Miroir fixe pour lecture manuelle immédiate
        latest_file = os.path.join(AUDIO_CACHE_DIR, "latest_speech.mp3")
        try:
            with open(audio_file, "rb") as src_f, open(latest_file, "wb") as dst_f:
                dst_f.write(src_f.read())
        except Exception as e:
            print(f"[TTS Mirror Error] {e}", file=sys.stderr)

        if auto_play:
            play_audio(audio_file)
    except Exception as e:
        print(f"Erreur TTS: {e}", file=sys.stderr)
    finally:
        release_tts_lock()

def replay_latest():
    """Rejoue le dernier message vocal sans régénérer de calcul ni de tokens."""
    latest_file = os.path.join(AUDIO_CACHE_DIR, "latest_speech.mp3")
    if os.path.exists(latest_file):
        print(f"[TTS] Relecture manuelle : {latest_file}")
        play_audio(latest_file)
    else:
        print("[TTS] Aucun fichier latest_speech.mp3 disponible.")

def find_active_transcript() -> str:
    """Trouve le transcript le plus récemment modifié parmi toutes les sessions Antigravity."""
    pattern = r"C:\Users\amado\.gemini\antigravity\brain\*\.system_generated\logs\transcript.jsonl"
    files = glob.glob(pattern)
    if not files:
        return ""
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]

class TranscriptWatcher:
    """Surveille les nouveaux messages de réponse de l'assistant et les vocalise."""

    def __init__(self, voice: str = DEFAULT_VOICE):
        self.voice = voice
        self.current_transcript = ""
        self.last_pos = 0
        self.seen_step_indices = set()

    def update_transcript_target(self):
        latest = find_active_transcript()
        if latest and latest != self.current_transcript:
            self.current_transcript = latest
            raw_size = os.path.getsize(latest) if os.path.exists(latest) else 0
            self.seen_step_indices.clear()
            
            # Au démarrage, marquer tous les steps existants comme vus pour ne jamais rejouer l'ancien
            if os.path.exists(latest) and raw_size > 0:
                try:
                    with open(latest, "r", encoding="utf-8", errors="ignore") as f:
                        # Lire les 64 derniers Ko pour indexer les steps déjà émis
                        f.seek(max(0, raw_size - 65536))
                        for l in f:
                            l = l.strip()
                            if not l: continue
                            try:
                                d = json.loads(l)
                                if "step_index" in d:
                                    self.seen_step_indices.add(d["step_index"])
                            except Exception:
                                pass
                except Exception as e:
                    print(f"[Watcher Index Error] {e}")

            self.last_pos = raw_size
            print(f"[Watcher] Cible active : {latest} (Position: {self.last_pos}, Steps déjà indexés: {len(self.seen_step_indices)})")

    def check_new_responses(self):
        self.update_transcript_target()
        if not self.current_transcript or not os.path.exists(self.current_transcript):
            return

        current_size = os.path.getsize(self.current_transcript)
        if current_size <= self.last_pos:
            return

        with open(self.current_transcript, "r", encoding="utf-8", errors="ignore") as f:
            f.seek(self.last_pos)
            new_lines = f.readlines()
            self.last_pos = f.tell()

        for line in new_lines:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                step_idx = data.get("step_index")
                step_type = data.get("type")
                source = data.get("source")
                content = data.get("content", "")

                if step_idx in self.seen_step_indices:
                    continue
                self.seen_step_indices.add(step_idx)

                # Quand le modèle termine une réponse sans appel d'outil
                if step_type == "PLANNER_RESPONSE" and source == "MODEL":
                    tool_calls = data.get("tool_calls", [])
                    if not tool_calls and content:
                        print(f"\n[TTS] Élocution de la réponse de l'assistant (Step {step_idx})...")
                        speak(content, self.voice, auto_play=True)
            except Exception:
                pass

    def run_loop(self, poll_interval: float = 1.0):
        print(f"=== Antigravity Voice Daemon 2-en-1 Initialisé ===")
        print(f"Voix par défaut : {self.voice}")
        while True:
            try:
                self.check_new_responses()
            except Exception as e:
                print(f"Erreur loop: {e}")
            time.sleep(poll_interval)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--speak":
        raw_text = " ".join(sys.argv[2:])
        speak(raw_text)
    elif len(sys.argv) > 1 and sys.argv[1] == "--replay":
        replay_latest()
    else:
        voice = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_VOICE
        watcher = TranscriptWatcher(voice)
        watcher.run_loop()
