import grpc
from utils.worker_pb2 import TaskRequest  # Import generated protobuf messages
from utils.worker_pb2_grpc import WorkerServiceStub  # Import generated gRPC stub

def send_task_to_worker(worker_address: str, prompt: str) -> str:
    """
    Sends a prompt to the worker via gRPC and receives the AI model's response.

    Args:
        worker_address (str): The gRPC server address (e.g., "localhost:50051").
        prompt (str): The prompt/question to send.

    Returns:
        str: The AI model's response.
    """
    try:
        if not prompt.strip():
            return "❌ Error: Empty prompt received."

        print(f"📡 Sending request to worker at {worker_address}...")
        
        # Connect to the worker node via gRPC
        with grpc.insecure_channel(worker_address) as channel:
            stub = WorkerServiceStub(channel)

            # Send request
            request = TaskRequest(prompt=prompt)
            response = stub.ProcessTask(request)

            print("✅ Response received successfully!")
            return response.result

    except grpc.RpcError as e:
        print(f"❌ gRPC error: {e.code()} - {e.details()}")
        return f"Error: Unable to process request ({e.code()} - {e.details()})"

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        return "Error: An unexpected issue occurred."