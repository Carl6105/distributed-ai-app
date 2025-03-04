import os

RAY_CLUSTER_ADDRESS = os.getenv("RAY_CLUSTER_ADDRESS", "auto")
AI_MODEL_NAME = os.getenv("AI_MODEL_NAME", "mistralai/Mistral-7B-v0.1")
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))