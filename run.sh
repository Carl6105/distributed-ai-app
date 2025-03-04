#!/bin/bash

echo "🚀 Starting Ray Cluster..."
ray start --head --port=6379

echo "✅ Ray Cluster started successfully!"

echo "🔧 Starting Worker Nodes..."
python workers/worker.py &

echo "✅ Worker node started!"

echo "🌍 Starting API Server..."
uvicorn server.server:app --host 0.0.0.0 --port 8000 --log-level info

echo "✅ API Server is running!"