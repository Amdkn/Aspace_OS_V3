#!/usr/bin/env python3
import argparse, json, os, platform, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HOST_NAME = "com.aspace.machine_fabric.canary"

def get_manifest_path():
    sys_name = platform.system()
    home = Path(os.environ.get("HOME", "~")).expanduser()
    if sys_name == 'Linux':
        return home / ".config" / "google-chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"
    elif sys_name == 'Darwin':
        return home / "Library" / "Application Support" / "Google" / "Chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"
    elif sys_name == 'Windows':
        return Path(os.environ.get("LOCALAPPDATA", "")) / "Google" / "Chrome" / "User Data" / "NativeMessagingHosts" / f"{HOST_NAME}.json"
    raise RuntimeError(f"Unsupported OS: {sys_name}")

def register_host(manifest_path, target_manifest_path):
    if platform.system() == 'Windows':
        import winreg
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"Software\\Google\\Chrome\\NativeMessagingHosts\\{HOST_NAME}")
        try:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, str(manifest_path))
        finally:
            winreg.CloseKey(key)
    else:
        target_manifest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(manifest_path, target_manifest_path)

def unregister_host(target_manifest_path):
    if platform.system() == 'Windows':
        import winreg
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, f"Software\\Google\\Chrome\\NativeMessagingHosts\\{HOST_NAME}")
        except FileNotFoundError:
            pass
    else:
        try:
            target_manifest_path.unlink()
        except FileNotFoundError:
            pass

def build_host():
    src = HERE / "native_host"
    out = HERE / "native_publish"
    print(f"Building dotnet Native Messaging Host in {out}...")
    cp = subprocess.run(["dotnet", "publish", str(src / "ASpaceNativeHost.csproj"), "-c", "Release", "-r", "win-x64" if platform.system() == 'Windows' else ("linux-x64" if platform.system() == "Linux" else "osx-x64"), "--self-contained", "false", "-o", str(out)], text=True, capture_output=True)
    if cp.returncode:
        raise RuntimeError("dotnet publish failed: " + cp.stderr[-2000:])
    exe_name = "ASpaceNativeHost.exe" if platform.system() == 'Windows' else "ASpaceNativeHost"
    exe = out / exe_name
    if not exe.exists():
        raise RuntimeError("native host exe missing")
    return exe

def get_extension_id():
    manifest_path = HERE / "extension" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    pub_b64 = manifest.get("key")
    if not pub_b64:
        raise ValueError("manifest.json must contain a 'key' field for persistent extension ID")
    import base64, hashlib
    pub = base64.b64decode(pub_b64)
    digest = hashlib.sha256(pub).digest()[:16]
    return "".join(chr(ord("a")+n) for b in digest for n in (b>>4, b&15))

def cmd_install():
    print("Installing AMF M1 Browser Agent...")
    ext_id = get_extension_id()
    print(f"Extension ID: {ext_id}")

    host_exe = build_host()

    manifest_path = HERE / "native_host_manifest.json"
    manifest_path.write_text(json.dumps({
        "name": HOST_NAME,
        "description": "A'Space Machine Fabric M1",
        "path": str(host_exe),
        "type": "stdio",
        "allowed_origins": [f"chrome-extension://{ext_id}/"]
    }, indent=2) + "\n", encoding="utf-8")

    target_manifest = get_manifest_path()
    register_host(manifest_path, target_manifest)
    print("Installed successfully.")

def cmd_uninstall():
    print("Uninstalling AMF M1 Browser Agent...")
    target_manifest = get_manifest_path()
    unregister_host(target_manifest)
    print("Uninstalled successfully.")

def cmd_update():
    print("Updating AMF M1 Browser Agent...")
    cmd_install()

def main():
    parser = argparse.ArgumentParser(description="AMF M1 Browser Agent Setup")
    parser.add_argument("command", choices=["install", "uninstall", "update"])
    args = parser.parse_args()

    if args.command == "install":
        cmd_install()
    elif args.command == "uninstall":
        cmd_uninstall()
    elif args.command == "update":
        cmd_update()

if __name__ == "__main__":
    main()
