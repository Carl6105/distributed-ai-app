import ray
from models.model_loader import generate_response

@ray.remote
def process_request(prompt: str):
    return generate_response(prompt)