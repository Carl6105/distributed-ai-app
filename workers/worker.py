import ray
from models.model_loader import generate_response

# Initialize Ray cluster
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
        response = generate_response(prompt)
        return response
    except Exception as e:
        return f"❌ Error processing request: {e}"

if __name__ == "__main__":
    print("✅ Worker node is ready and waiting for tasks...")