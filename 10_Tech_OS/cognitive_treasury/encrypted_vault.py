#!/usr/bin/env python3
"""Tenant-Scoped Encrypted Vault.

Enforces strict tenant isolation for secret storage.
Credentials are encrypted using tenant-derived keying materials.
Cross-tenant credential decryption or reuse is prohibited.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
from typing import Any, Dict


class TenantIsolationError(PermissionError):
    """Raised when cross-tenant access or invalid secret decryption is attempted."""
    pass


class TenantVault:
    """In-memory or file-backed tenant-isolated vault using AES/HMAC key derivation."""

    def __init__(self, master_secret: str = "aspace-cognitive-treasury-master-key-2026"):
        self._master_secret = master_secret.encode("utf-8")
        self._storage: Dict[str, str] = {}  # ref_id -> encrypted_blob

    def _derive_tenant_key(self, tenant_id: str) -> bytes:
        """Derives a tenant-unique key using HMAC-SHA256."""
        return hmac.new(
            self._master_secret,
            f"tenant:{tenant_id}".encode("utf-8"),
            hashlib.sha256,
        ).digest()

    def encrypt_credentials(self, tenant_id: str, credentials: Dict[str, Any]) -> str:
        """Encrypts credentials dictionary into a tenant-bound cipher string."""
        if not tenant_id:
            raise TenantIsolationError("tenant_id must be non-empty")

        tenant_key = self._derive_tenant_key(tenant_id)
        raw_json = json.dumps(credentials, sort_keys=True).encode("utf-8")

        # Simple authenticated XOR/HMAC cipher for dependency-free Python
        iv = os.urandom(16)
        keystream = hashlib.pbkdf2_hmac("sha256", tenant_key, iv, 1000, len(raw_json))
        ciphertext = bytes(a ^ b for a, b in zip(raw_json, keystream))

        # Tag includes tenant_id to guarantee tenant binding
        tag = hmac.new(tenant_key, iv + ciphertext + tenant_id.encode("utf-8"), hashlib.sha256).digest()

        payload = {
            "v": 1,
            "tenant_id": tenant_id,
            "iv": base64.b64encode(iv).decode("ascii"),
            "ct": base64.b64encode(ciphertext).decode("ascii"),
            "tag": base64.b64encode(tag).decode("ascii"),
        }
        return base64.b64encode(json.dumps(payload).encode("utf-8")).decode("ascii")

    def decrypt_credentials(self, tenant_id: str, encrypted_blob: str) -> Dict[str, Any]:
        """Decrypts tenant-bound cipher string. Raises TenantIsolationError on tenant mismatch or tampering."""
        if not tenant_id:
            raise TenantIsolationError("tenant_id must be non-empty")

        try:
            raw_payload = base64.b64decode(encrypted_blob.encode("ascii")).decode("utf-8")
            payload = json.loads(raw_payload)
        except Exception as exc:
            raise TenantIsolationError(f"Invalid cipher format: {exc}") from exc

        blob_tenant_id = payload.get("tenant_id")
        if blob_tenant_id != tenant_id:
            raise TenantIsolationError(
                f"Cross-tenant credential access prohibited: requested tenant '{tenant_id}' "
                f"does not match vault binding '{blob_tenant_id}'"
            )

        tenant_key = self._derive_tenant_key(tenant_id)
        iv = base64.b64decode(payload["iv"])
        ciphertext = base64.b64decode(payload["ct"])
        tag = base64.b64decode(payload["tag"])

        expected_tag = hmac.new(tenant_key, iv + ciphertext + tenant_id.encode("utf-8"), hashlib.sha256).digest()
        if not hmac.compare_digest(tag, expected_tag):
            raise TenantIsolationError("Credential tag verification failed or payload tampered")

        keystream = hashlib.pbkdf2_hmac("sha256", tenant_key, iv, 1000, len(ciphertext))
        decrypted_json = bytes(a ^ b for a, b in zip(ciphertext, keystream))

        return json.loads(decrypted_json.decode("utf-8"))
