#!/bin/bash

# 🚀 Zero Trust FS Minimal Pipeline - Fully Automatic Setup

echo "=== Zero Trust FS Minimal Pipeline ==="
echo "Checking and installing dependencies..."

# 1️⃣ Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found. Please install Python 3 manually."
    exit 1
fi

# 2️⃣ Ensure pip3 is available
if ! command -v pip3 &> /dev/null
then
    echo "⚠️ pip3 not found. Attempting to install..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update && sudo apt-get install -y python3-pip
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python3
    else
        echo "❌ pip3 installation not automated for this OS."
        exit 1
    fi
fi

# 3️⃣ Install Python dependencies
echo "Installing Python modules..."
python3 -m pip install --quiet --upgrade pip
python3 -m pip install --quiet pyyaml

# 4️⃣ Create minimal files folder if not exists
if [ ! -d "files" ]; then
    echo "Creating 'files' folder for test files..."
    mkdir files
    # Create some example files
    echo "Top Secret Report" > files/secret_report.txt
    echo "Editable Document" > files/edit_document.txt
    echo "Public Note" > files/public_note.txt
fi

# 5️⃣ Run the main Python pipeline
echo "Starting Zero Trust FS..."
python3 main.py
