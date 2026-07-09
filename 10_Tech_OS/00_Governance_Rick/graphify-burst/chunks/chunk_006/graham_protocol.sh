#!/bin/bash
# 03_Graham_Backup (The Archivist)
# Runs Daily (04:00 AM).
# Mission: Snapshot OpenClaw and Identity Core to Cloud.

echo "--- GRAHAM PROTOCOL STARTED ---"
date

BACKUP_DIR="/tmp/backup_$(date +%F)"
TARGET_DIR="/root/aspace_a0_amadeus"
ARCHIVE_NAME="amadeus_backup_$(date +%F).tar.gz"

# 1. Prepare
mkdir -p $BACKUP_DIR
echo "📦 Preparing Backup for $TARGET_DIR..."

# 2. Stop Services (Optional - to ensure data consistency)
# echo "🛑 Stopping OpenClaw..."
# docker stop openclaw

# 3. Compress
echo "🗜️ Compressing Data..."
tar -czf "$BACKUP_DIR/$ARCHIVE_NAME" "$TARGET_DIR"

# 4. Upload (Simulated Rclone)
echo "☁️ Uploading to Secure Storage..."
# rclone copy "$BACKUP_DIR/$ARCHIVE_NAME" remote:backups/
echo "✅ Upload Simulated."

# 5. Cleanup
rm -rf $BACKUP_DIR
# docker start openclaw

echo "--- GRAHAM PROTOCOL COMPLETE ---"
