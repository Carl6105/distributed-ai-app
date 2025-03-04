#!/bin/bash

echo "🔧 Setting up Worker Node..."

# 1️⃣ Install Python (if not installed)
if ! command -v python3 &>/dev/null; then
    echo "🚀 Installing Python..."
    sudo apt update && sudo apt install -y python3 python3-pip
fi

# 2️⃣ Upgrade pip
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip

# 3️⃣ Install necessary Python libraries
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# 4️⃣ Install Ray
echo "⚙️ Installing Ray..."
pip install "ray[default]"

# 5️⃣ Connect worker to Ray Cluster (Change MAIN_SERVER_IP)
MAIN_SERVER_IP="172.50.2.4"
echo "🔗 Connecting to Ray Cluster at $MAIN_SERVER_IP..."
ray start --address=$MAIN_SERVER_IP:6379

# 6️⃣ Start the worker process
echo "🚀 Starting Worker Node..."
python workers/worker.py
