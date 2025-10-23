#!/usr/bin/env bash
# NASA PDF Downloader Script
# Downloads NASA technical report from NTRS (NASA Technical Reports Server)

set -e  # Exit on any error

# Configuration
URL="https://ntrs.nasa.gov/api/citations/19720063753/downloads/19720063753.pdf"
FILENAME="19720063753.pdf"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🚀 NASA PDF Downloader"
echo "======================"
echo "Target URL: $URL"
echo "Output file: $FILENAME"
echo "Download directory: $SCRIPT_DIR"
echo ""

# Check if file already exists
if [ -f "$SCRIPT_DIR/$FILENAME" ]; then
    echo "⚠️  File $FILENAME already exists in $SCRIPT_DIR"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Download cancelled."
        exit 0
    fi
fi

# Function to download with curl
download_with_curl() {
    echo "📥 Downloading with curl..."
    if curl -L -f -o "$SCRIPT_DIR/$FILENAME" "$URL" --progress-bar; then
        return 0
    else
        return 1
    fi
}

# Function to download with wget
download_with_wget() {
    echo "📥 Downloading with wget..."
    if wget -O "$SCRIPT_DIR/$FILENAME" "$URL" --progress=bar:force; then
        return 0
    else
        return 1
    fi
}

# Try downloading with available tools
if command -v curl >/dev/null 2>&1; then
    if download_with_curl; then
        echo "✅ Download completed successfully with curl!"
    elif command -v wget >/dev/null 2>&1; then
        echo "⚠️  curl failed, trying wget..."
        if download_with_wget; then
            echo "✅ Download completed successfully with wget!"
        else
            echo "❌ Both curl and wget failed to download the file."
            exit 1
        fi
    else
        echo "❌ curl failed and wget is not available."
        exit 1
    fi
elif command -v wget >/dev/null 2>&1; then
    if download_with_wget; then
        echo "✅ Download completed successfully with wget!"
    else
        echo "❌ wget failed to download the file."
        exit 1
    fi
else
    echo "❌ Neither curl nor wget is available. Please install one of them."
    exit 1
fi

# Verify the downloaded file
if [ -f "$SCRIPT_DIR/$FILENAME" ]; then
    FILE_SIZE=$(stat -f%z "$SCRIPT_DIR/$FILENAME" 2>/dev/null || stat -c%s "$SCRIPT_DIR/$FILENAME" 2>/dev/null || echo "unknown")
    echo ""
    echo "📊 Download Summary:"
    echo "   File: $FILENAME"
    echo "   Size: $FILE_SIZE bytes"
    echo "   Location: $SCRIPT_DIR/$FILENAME"
    
    # Basic PDF validation
    if file "$SCRIPT_DIR/$FILENAME" | grep -q "PDF"; then
        echo "   Type: ✅ Valid PDF file"
    else
        echo "   Type: ⚠️  Warning: File may not be a valid PDF"
    fi
else
    echo "❌ Error: Downloaded file not found!"
    exit 1
fi

echo ""
echo "🎉 NASA technical report download complete!"