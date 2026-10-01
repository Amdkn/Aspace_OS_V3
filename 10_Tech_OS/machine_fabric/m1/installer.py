#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HOST_NAME = "com.aspace.machine_fabric.m1"
DEFAULT_EXTENSION_ID = "occamkcdejbkfmobilobgcloapndicjk"
HERE = Path(__file__).parent.resolve()
NATIVE_HOST_SRC = HERE / "native_host"
NATIVE_HOST_BIN = HERE / "native_host_bin"
EXTENSION_SRC = HERE / "extension"

if sys.platform == "win32":
    import winreg

def get_manifest_path():
    if sys.platform == "win32":
        return Path(os.environ.get("LOCALAPPDATA", "")) / "Aspace" / "NativeMessaging" / f"{HOST_NAME}.json"
    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"
    else:
        return Path.home() / ".config" / "google-chrome" / "NativeMessagingHosts" / f"{HOST_NAME}.json"

def get_extension_install_dir():
    override = os.environ.get("ASPACE_EXTENSION_DIR")
    if override:
        return Path(override)
    if sys.platform == "win32":
        return Path(os.environ.get("LOCALAPPDATA", "")) / "Aspace" / "Extension"
    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "Aspace" / "Extension"
    else:
        return Path.home() / ".config" / "aspace" / "extension"

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
            print(f"Warning: Failed to set Windows Registry for NativeMessaging: {e}")

    print(f"Manifest installed at: {manifest_path}")

def install_extension(extension_id):
    src_dir = EXTENSION_SRC
    install_dir = get_extension_install_dir()
    install_dir.mkdir(parents=True, exist_ok=True)

    # Copy extension files to stable location
    if src_dir.exists():
        for item in src_dir.glob("*"):
            if item.is_file():
                shutil.copy2(item, install_dir / item.name)

    # Read version from manifest
    manifest_file = install_dir / "manifest.json"
    version = "1.0.0"
    if manifest_file.exists():
        try:
            m = json.loads(manifest_file.read_text(encoding="utf-8"))
            version = m.get("version", "1.0.0")
        except Exception:
            pass

    # Register external extension in Chrome
    if sys.platform == "win32":
        ext_key_path = f"Software\\Google\\Chrome\\Extensions\\{extension_id}"
        try:
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, ext_key_path)
            winreg.SetValueEx(key, "path", 0, winreg.REG_SZ, str(install_dir))
            winreg.SetValueEx(key, "version", 0, winreg.REG_SZ, version)
            winreg.CloseKey(key)
        except Exception as e:
            print(f"Warning: Failed to set Chrome Extension registry key: {e}")
    elif sys.platform != "darwin":
        ext_dir = Path.home() / ".config" / "google-chrome" / "External Extensions"
        ext_dir.mkdir(parents=True, exist_ok=True)
        ext_json = ext_dir / f"{extension_id}.json"
        ext_json.write_text(json.dumps({"path": str(install_dir), "version": version}, indent=2) + "\n", encoding="utf-8")

    print(f"Extension installed at: {install_dir} (id: {extension_id})")

def install(args):
    print("Installing...")
    exe_path = compile_host()
    install_manifest(exe_path, args.extension_id)
    install_extension(args.extension_id)
    print("Install complete.")

def update(args):
    print("Updating...")
    exe_path = compile_host()
    install_manifest(exe_path, args.extension_id)
    install_extension(args.extension_id)
    print("Update complete.")

def uninstall(args):
    print("Uninstalling...")
    manifest_path = get_manifest_path()
    if manifest_path.exists():
        manifest_path.unlink()
        print(f"Removed manifest: {manifest_path}")

    ext_id = getattr(args, "extension_id", DEFAULT_EXTENSION_ID)

    if sys.platform == "win32":
        key_path = f"Software\\Google\\Chrome\\NativeMessagingHosts\\{HOST_NAME}"
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)
            print(f"Removed registry key: {key_path}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Failed to remove Windows Registry key: {e}")

        ext_key_path = f"Software\\Google\\Chrome\\Extensions\\{ext_id}"
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, ext_key_path)
            print(f"Removed Chrome Extension registry key: {ext_key_path}")
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Failed to remove Chrome Extension registry key: {e}")
    elif sys.platform != "darwin":
        ext_json = Path.home() / ".config" / "google-chrome" / "External Extensions" / f"{ext_id}.json"
        if ext_json.exists():
            ext_json.unlink()
            print(f"Removed external extension json: {ext_json}")

    install_dir = get_extension_install_dir()
    if install_dir.exists():
        shutil.rmtree(install_dir, ignore_errors=True)
        print(f"Removed installed extension directory: {install_dir}")

    if NATIVE_HOST_BIN.exists():
        shutil.rmtree(NATIVE_HOST_BIN, ignore_errors=True)
        print("Removed compiled binaries.")

    print("Uninstall complete.")

def main():
    parser = argparse.ArgumentParser(description="A'Space Machine Fabric M1 Production Installer")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_install = subparsers.add_parser("install", help="Install Native Messaging Host and Extension")
    p_install.add_argument("--extension-id", default=DEFAULT_EXTENSION_ID, help="Chrome Extension ID")

    p_update = subparsers.add_parser("update", help="Update Native Messaging Host and Extension")
    p_update.add_argument("--extension-id", default=DEFAULT_EXTENSION_ID, help="Chrome Extension ID")

    p_uninstall = subparsers.add_parser("uninstall", help="Uninstall Native Messaging Host and Extension")
    p_uninstall.add_argument("--extension-id", default=DEFAULT_EXTENSION_ID, help="Chrome Extension ID")

    args = parser.parse_args()

    if args.command == "install":
        install(args)
    elif args.command == "update":
        update(args)
    elif args.command == "uninstall":
        uninstall(args)

if __name__ == "__main__":
    main()
