import ray
from models.model_loader import generate_response

# Initialize Ray cluster
if not ray.is_initialized():
    ray.init(address="auto", ignore_reinit_error=True)

@ray.remote
def worker_task(prompt: str) -> str:
    """
    Remote function executed by worker nodes.

    Args:
        prompt (str): The input prompt for the AI model.

    Returns:
        str: The AI-generated response.
    """
    try:
        if not prompt.strip():
            return "❌ Error: Received an empty prompt."

        print(f"📩 Processing task: {prompt[:50]}...")  # Log first 50 characters
        response = generate_response(prompt)
        print("✅ Task completed successfully!")

        return response
    except Exception as e:
        print(f"⚠️ Error in worker_task: {e}")
        return f"❌ Error processing request: {e}"

if __name__ == "__main__":
    print("✅ Worker node is ready and waiting for tasks...")