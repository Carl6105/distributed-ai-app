import ray
import sys
import os

# Ensure correct module import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.model_loader import generate_response  # Adjusted import path

# Initialize Ray (only if not already initialized)
if not ray.is_initialized():
    ray.init(address="auto")

@ray.remote
def process_request(prompt: str):
    """
    Process a prompt using the AI model running on distributed workers.

    Args:
        prompt (str): The input prompt from the user.

    Returns:
        str: The AI-generated response.
    """
    try:
        return generate_response(prompt)
    except Exception as e:
        print(f"⚠️ Error processing prompt: {e}")
        return "⚠️ Error: Failed to process the request."