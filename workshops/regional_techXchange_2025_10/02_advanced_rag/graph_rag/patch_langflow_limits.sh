#!/usr/bin/env bash
set -e

# Locate the langflow installation
SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])" 2>/dev/null || python -c "import site; print(site.getusersitepackages())")
TARGET_FILE="$SITE_PACKAGES/langflow/serialization/constants.py"

# Verify file exists
if [ ! -f "$TARGET_FILE" ]; then
  echo "Langflow constants.py not found in $SITE_PACKAGES"
  exit 1
fi

# Apply patch
echo "Patching $TARGET_FILE..."
sed -i.bak \
  -e 's/^MAX_TEXT_LENGTH = .*/MAX_TEXT_LENGTH = 60000/' \
  -e 's/^MAX_ITEMS_LENGTH = .*/MAX_ITEMS_LENGTH = 10000/' \
  "$TARGET_FILE"

echo "Patch applied. Backup saved as constants.py.bak"