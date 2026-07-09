# 99_Container_Vault (The Cargo Bay)

**The Storage of Persistent Data.**
This is where the Docker Volumes live. The precious cargo.

---

## 📦 Role: The Hold
*   **Content**: Database files (`/var/lib/postgresql`), Config files, Uploads.
*   **Rule**: **This folder is backed up.** Everything else is ephemeral.

## 💾 Backup Strategy (12th Doctor's Domain)
*   **Restic**: Snapshot backups to S3/B2.
*   **Frequency**: Daily (Incremental).
*   **Retention**: Keep 7 days, 4 weeks, 6 months.
