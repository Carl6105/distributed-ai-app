from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import ray
import json
import sys
import os

# Ensure proper module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from server.task_manager import process_request  # Adjusted import path

# Initialize Ray (only if not already initialized)
if not ray.is_initialized():
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

            # Extract prompt safely
            prompt = request.get("prompt", "").strip()
            if not prompt:
                await websocket.send_text(json.dumps({"error": "Empty prompt received"}))
                continue

            print(f"📩 Received prompt: {prompt}")

            # Send query to worker and fetch response
            try:
                result = process_request.remote(prompt)
                response = ray.get(result)  # Fetch result from Ray worker

                # Send response back to client
                await websocket.send_text(json.dumps({"response": response}))
                print(f"✅ Response sent to client!")

            except Exception as process_error:
                print(f"⚠️ Error processing request: {process_error}")
                await websocket.send_text(json.dumps({"error": "Processing error occurred"}))

    except WebSocketDisconnect:
        print("❌ Client disconnected!")
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON received!")
        await websocket.send_text(json.dumps({"error": "Invalid JSON format"}))
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        await websocket.send_text(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)