from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import ray
import json
from task_manager import process_request

# Initialize Ray
ray.init(address="auto")

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("✅ Client connected to WebSocket!")

    try:
        while True:
            data = await websocket.receive_text()
            request = json.loads(data)
            prompt = request.get("prompt", "")

            if not prompt:
                await websocket.send_text(json.dumps({"error": "Empty prompt received"}))
                continue

            print(f"📩 Received prompt: {prompt}")

            # Send query to worker
            result = process_request.remote(prompt)
            response = ray.get(result)

            # Send response back to client
            await websocket.send_text(json.dumps({"response": response}))
            print(f"✅ Response sent to client!")

    except WebSocketDisconnect:
        print("❌ Client disconnected!")
    except Exception as e:
        print(f"⚠️ Error: {e}")
        await websocket.send_text(json.dumps({"error": str(e)}))