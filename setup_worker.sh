#!/bin/bash

# Stop script on first error
set -e

echo "🔧 Setting up Worker Node..."

# 1️⃣ Install Python (if not installed)
if ! command -v python3 &>/dev/null; then
    echo "🚀 Installing Python..."
    sudo apt update && sudo apt install -y python3 python3-pip
else
    echo "✅ Python is already installed."
fi

# 2️⃣ Upgrade pip
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip

# 3️⃣ Install necessary Python libraries
if [[ -f "requirements.txt" ]]; then
    echo "📦 Installing dependencies from requirements.txt..."
    pip install --no-cache-dir -r requirements.txt
else
    echo "⚠️ Warning: requirements.txt not found! Skipping dependency installation."
fi

# 4️⃣ Install Ray
if ! python3 -c "import ray" &>/dev/null; then
    echo "⚙️ Installing Ray..."
    pip install "ray[default]"
else
    echo "✅ Ray is already installed."
fi

# 5️⃣ Connect worker to Ray Cluster (Change MAIN_SERVER_IP)
MAIN_SERVER_IP="172.50.2.4"

echo "🔗 Checking Ray Cluster connection..."
if ping -c 1 -W 1 $MAIN_SERVER_IP &>/dev/null; then
    echo "✅ Ray Cluster is reachable. Connecting..."
    ray start --address=$MAIN_SERVER_IP:6379
else
    echo "❌ Error: Ray Cluster is not reachable at $MAIN_SERVER_IP! Check your network."
    exit 1
fi

# 6️⃣ Start the worker process
echo "🚀 Starting Worker Node..."
python workers/worker.py

echo "✅ Worker setup completed!"