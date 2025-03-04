#!/bin/bash

# Stop script on first error
set -e

echo "🚀 Starting Ray Cluster..."
# Check if Ray is already running before starting
if ! ray status &>/dev/null; then
    ray start --head --port=6379
    echo "✅ Ray Cluster started successfully!"
else
    echo "⚠️ Ray Cluster is already running."
fi

echo "🔧 Starting Worker Nodes..."
python workers/worker.py &

# Capture the Worker PID to monitor
WORKER_PID=$!
echo "✅ Worker node started! (PID: $WORKER_PID)"

echo "🌍 Starting API Server..."
uvicorn server.server:app --host 0.0.0.0 --port 8000 --log-level info &

# Capture the API Server PID
SERVER_PID=$!
echo "✅ API Server is running! (PID: $SERVER_PID)"

# Trap script exit and clean up background processes
trap "echo '🛑 Stopping services...'; kill $WORKER_PID $SERVER_PID; ray stop; exit 0" SIGINT SIGTERM

# Keep script running to monitor processes
wait $WORKER_PID $SERVER_PID