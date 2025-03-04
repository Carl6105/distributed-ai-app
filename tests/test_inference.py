from models.model_loader import generate_response

def test_model():
    try:
        print("⏳ Running AI Model Inference Test...")

        # Basic test
        prompt = "Explain quantum physics in simple words."
        response = generate_response(prompt)
        assert isinstance(response, str) and len(response) > 0
        print("✅ Basic Test Passed!")

        # Test for empty input
        empty_response = generate_response("")
        assert isinstance(empty_response, str), "❌ Model should return a string for empty input."
        print("✅ Empty Input Test Passed!")

        # Test for long input
        long_prompt = "What are the key differences between classical and quantum mechanics?" * 5
        long_response = generate_response(long_prompt)
        assert isinstance(long_response, str) and len(long_response) > 0
        print("✅ Long Input Test Passed!")

        print("🎉 All AI Model Inference Tests Passed!")

    except AssertionError as error:
        print(f"❌ Test failed: {error}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_model()