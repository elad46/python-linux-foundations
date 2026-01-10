#!/bin/bash

SOURCE_DIR="$HOME"
BACKUP_DIR="$HOME/backups"
DATE=$(date +"%Y-%m-%d")

mkdir -p "$BACKUP_DIR"

tar -czvf "$BACKUP_DIR/home_backup_$DATE.tar.gz" "$SOURCE_DIR"

echo "Backup completed: $BACKUP_DIR/home_backup_$DATE.tar.gz"
