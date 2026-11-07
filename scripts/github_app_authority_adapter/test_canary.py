#!/usr/bin/env python3
"""
A'Space GitHub App Authority Adapter - Canary Test

Run this to verify the authority adapter canary setup for issue #555.
Tests:
1. Webhook HMAC SHA-256 signature verification
2. Delivery ID dedupe
3. Authority resolution (installation vs user token)
4. Projects V2 authority classification
5. Receipt persistence
"""

import json
import sys
from pathlib import Path

# Add the adapter directory to the path
adapter_dir = Path(__file__).parent  # scripts/github_app_authority_adapter
project_root = adapter_dir.parent  # scripts/
sys.path.insert(0, str(adapter_dir))
sys.path.insert(0, str(project_root))

# Import modules directly
import install_authority_adapter
from github_webhook_handler import GitHubWebhookHandler, test_webhook_handler


def verify_installations():
    """Verify that the canary files exist and are properly structured."""
    print("=" * 60)
    print("Verifying Authority Adapter Canary Setup")
    print("=" * 60)

    required_files = [
        "install_authority_adapter.py",
        "github_authority_resolver.py",
        "github_webhook_handler.py",
    ]

    optional_files = [
        ".gh_app_private_key.pem",
        ".gh_app_webhook_secret",
        ".gh_app_installation_token",
        ".github_app_receipt.json",
    ]

    print("\nRequired files:")
    for f in required_files:
        exists = (adapter_dir / f).exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {f}")

    print("\nOptional (canary artifacts):")
    for f in optional_files:
        exists = (adapter_dir / f).exists()
        status = "✓" if exists else "✗"
        print(f"  {status} {f}")

    # Check git status - private key should NOT be committed
    print("\nGit check (private key should be gitignored):")
    try:
        result = subprocess.run(
            ["git", "check-ignore", str(adapter_dir / ".gh_app_private_key.pem")],
            capture_output=True, text=True, cwd="."
        )
        if result.returncode == 0:
            print("  ✓ Private key would be gitignored")
        else:
            print("  ! Private key not in .gitignore (may need addition)")
    except Exception:
        print("  ? Could not check gitignore")

    # Verify key files are not in git
    print("\nChecking private key is not tracked by git:")
    try:
        result = subprocess.run(
            ["git", "ls-files", str(adapter_dir / ".gh_app_private_key.pem")],
            capture_output=True, text=True, cwd="."
        )
        if result.stdout.strip():
            print("  ✗ Private key IS tracked by git - THIS IS A SECURITY ISSUE")
        else:
            print("  ✓ Private key is NOT tracked by git")
    except Exception:
        print("  ? Could not check git ls-files")


def main():
    """Entry point for the canary test."""
    verify_installations()
    test_webhook_handler()
    print("\n" + "=" * 60)
    print("Canary test complete")
    print("=" * 60)


if __name__ == "__main__":
    main()