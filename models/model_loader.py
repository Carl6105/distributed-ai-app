from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
from config.settings import AI_MODEL_NAME
import torch
import os

# Load Hugging Face API token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

# Authenticate if token is available
if HF_TOKEN:
    try:
        login(HF_TOKEN)
        print("🔑 Hugging Face authentication successful!")
    except Exception as e:
        print(f"⚠️ Authentication failed: {e}")
else:
    print("⚠️ Hugging Face token not found. Ensure you have access to the model.")

try:
    # Load tokenizer
    print("⏳ Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(AI_MODEL_NAME)
    print("✅ Tokenizer loaded successfully!")
except Exception as e:
    print(f"❌ Error loading tokenizer: {e}")
    tokenizer = None

try:
    # Set device configuration (CUDA if available, otherwise CPU)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32

    # Load model with automatic device placement
    print(f"⏳ Loading model on {device}...")
    model = AutoModelForCausalLM.from_pretrained(AI_MODEL_NAME, torch_dtype=dtype, device_map="auto")
    model.to(device)  # Ensure the model is explicitly moved to the device
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# Function to generate a response from the model
def generate_response(prompt: str):
    if model is None or tokenizer is None:
        return "❌ Model is not loaded."

    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)  # Move input to the correct device
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=500)

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        print(f"⚠️ Error during inference: {e}")
        return "❌ Error generating response."