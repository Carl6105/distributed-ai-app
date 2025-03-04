Distributed AI Model App 🚀
This project utilizes Mistral 7B with Ray Distributed to efficiently process AI tasks across multiple devices. It enables distributed AI inference, making large language models accessible with shared compute power.

📌 Features
✅ Distributed AI processing using Ray
✅ Model inference with Mistral 7B
✅ Scalable architecture with worker nodes
✅ REST API & WebSocket support for real-time communication

🛠️ Setup Instructions
1️⃣ Install Dependencies
Ensure Python 3.8+ is installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Start the Main Server
bash
Copy
Edit
./run.sh
This will:
✅ Start the Ray Cluster
✅ Launch the worker nodes
✅ Start the FastAPI server

3️⃣ Run a Test Query
To check if the server is working, send a test request:

bash
Copy
Edit
curl -X POST "http://localhost:8000/query/" -d '{"prompt": "What is AI?"}'
If successful, you’ll receive an AI-generated response.

💻 Setting Up a Worker Node
On the worker device, clone the repository and run:

bash
Copy
Edit
git clone https://github.com/Carl6105/distributed-ai-app.git
cd distributed-ai-app
chmod +x setup_worker.sh
./setup_worker.sh
This will install dependencies and connect the worker to the main Ray Cluster.

🛠️ Available Endpoints
1️⃣ WebSocket API (ws://localhost:8000/ws)
For real-time streaming responses.

2️⃣ REST API (POST /query/)
For sending requests and receiving responses.

🔹 Author: Carl
🔹 License: MIT
🔹 Contributions: Open to pull requests!