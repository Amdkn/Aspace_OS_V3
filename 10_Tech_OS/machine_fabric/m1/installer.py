#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HOST_NAME = "com.aspace.machine_fabric.m1"
HERE = Path(__file__).parent.resolve()
NATIVE_HOST_SRC = HERE / "native_host"
DEPLOY_DIR = Path.home() / ".aspace" / "dc" / "chrome-extension-prod"
NATIVE_HOST_BIN = DEPLOY_DIR / "native_host_bin"
EXTENSION_SRC = HERE / "extension"
EXTENSION_DEPLOY = DEPLOY_DIR / "extension"

if sys.platform == "win32":
    import winreg

def get_manifest_path():
    if sys.platform == "win32":
        return Path(os.environ.get("LOCALAPPDATA", "")) / "Aspace" / "NativeMessaging" / f"{HOST_NAME}.json"
    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"
    else:
        return Path.home() / ".config" / "google-chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"

def compile_host():
    print("Compiling Native Messaging Host...")
    out_dir = NATIVE_HOST_BIN
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run(["dotnet", "publish", str(NATIVE_HOST_SRC), "-c", "Release", "-o", str(out_dir), "-r", "win-x64" if sys.platform == "win32" else "linux-x64", "--self-contained", "false"], check=True, stdout=subprocess.DEVNULL)
        exe_path = out_dir / ("ASpaceNativeHost.exe" if sys.platform == "win32" else "ASpaceNativeHost")
        return exe_path
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        if os.environ.get("CI_TESTING_INSTALLER"):
            print("CI: Mocking Native Messaging Host compilation.")
            dummy_exe = out_dir / ("ASpaceNativeHost.exe" if sys.platform == "win32" else "ASpaceNativeHost")
            dummy_exe.touch()
            if sys.platform != "win32":
                dummy_exe.chmod(0o755)
            return dummy_exe
        print(f"Error: 'dotnet' not found or compilation failed: {e}", file=sys.stderr)
        sys.exit(1)

def install_manifest(exe_path, extension_id):
    manifest_path = get_manifest_path()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    manifest_data = {
        "name": HOST_NAME,
        "description": "A'Space Machine Fabric M1 Production Host",
        "path": str(exe_path),
        "type": "stdio",
        "allowed_origins": [f"chrome-extension://{extension_id}/"]
    }

    manifest_path.write_text(json.dumps(manifest_data, indent=2) + "\n", encoding="utf-8")

    if sys.platform == "win32":
        key_path = f"Software\\Google\\Chrome\\NativeMessagingHosts\\{HOST_NAME}"
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, str(manifest_path))
            winreg.CloseKey(key)
        except Exception as e:
            print(f"Warning: Failed to set Windows Registry: {e}")

    print(f"Manifest installed at: {manifest_path}")

def install(args):
    print("Installing...")
    DEPLOY_DIR.mkdir(parents=True, exist_ok=True)
    if EXTENSION_DEPLOY.exists():
        shutil.rmtree(EXTENSION_DEPLOY, ignore_errors=True)
    shutil.copytree(EXTENSION_SRC, EXTENSION_DEPLOY)
    print(f"Extension deployed to: {EXTENSION_DEPLOY}")
    exe_path = compile_host()
    install_manifest(exe_path, args.extension_id)
    print("Install complete.")

def update(args):
    print("Updating...")
    if EXTENSION_DEPLOY.exists():
        shutil.rmtree(EXTENSION_DEPLOY, ignore_errors=True)
    shutil.copytree(EXTENSION_SRC, EXTENSION_DEPLOY)
    print(f"Extension deployed to: {EXTENSION_DEPLOY}")
    exe_path = compile_host()
    install_manifest(exe_path, args.extension_id)
    print("Update complete.")

def uninstall(args):
    print("Uninstalling...")
    manifest_path = get_manifest_path()
    if manifest_path.exists():
        manifest_path.unlink()
        print(f"Removed manifest: {manifest_path}")

    if sys.platform == "win32":
        key_path = f"Software\\Google\\Chrome\\NativeMessagingHosts\\{HOST_NAME}"
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
            print(f"Removed registry key: {key_path}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Failed to remove Windows Registry key: {e}")

    if DEPLOY_DIR.exists():
        shutil.rmtree(DEPLOY_DIR, ignore_errors=True)
        print("Removed deployed extension and compiled binaries.")

    print("Uninstall complete.")

def main():
    parser = argparse.ArgumentParser(description="A'Space Machine Fabric M1 Production Installer")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_install = subparsers.add_parser("install", help="Install Native Messaging Host and Extension")
    p_install.add_argument("--extension-id", default="occamkcdejbkfmobilobgcloapndicjk", help="Chrome Extension ID")

    p_update = subparsers.add_parser("update", help="Update Native Messaging Host and Extension")
    p_update.add_argument("--extension-id", default="occamkcdejbkfmobilobgcloapndicjk", help="Chrome Extension ID")

    p_uninstall = subparsers.add_parser("uninstall", help="Uninstall Native Messaging Host")

    args = parser.parse_args()

    if args.command == "install":
        install(args)
    elif args.command == "update":
        update(args)
    elif args.command == "uninstall":
        uninstall(args)

if __name__ == "__main__":
    main()
