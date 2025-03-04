from models.model_loader import generate_response

def test_model():
    """
    Runs multiple test cases to validate the AI model's response generation.
    """
    try:
        print("\n🧪 Running AI Model Inference Tests...\n")

        # ✅ Basic test with a standard prompt
        prompt = "Explain quantum physics in simple words."
        response = generate_response(prompt)
        assert isinstance(response, str) and len(response.strip()) > 0, "❌ Basic test failed: Empty response."
        print("✅ Basic Test Passed!")

        # ✅ Test for empty input
        empty_response = generate_response("")
        assert isinstance(empty_response, str), "❌ Empty input test failed: Model should return a string."
        print("✅ Empty Input Test Passed!")

        # ✅ Test for long input
        long_prompt = "What are the key differences between classical and quantum mechanics? " * 5
        long_response = generate_response(long_prompt)
        assert isinstance(long_response, str) and len(long_response.strip()) > 0, "❌ Long input test failed: Empty response."
        print("✅ Long Input Test Passed!")

        # ✅ Test for non-English input
        foreign_prompt = "¿Cómo funciona la inteligencia artificial?"
        foreign_response = generate_response(foreign_prompt)
        assert isinstance(foreign_response, str) and len(foreign_response.strip()) > 0, "❌ Foreign language test failed."
        print("✅ Foreign Language Test Passed!")

        # ✅ Test for code-related input
        code_prompt = "Write a Python function to reverse a string."
        code_response = generate_response(code_prompt)
        assert isinstance(code_response, str) and "def" in code_response.lower(), "❌ Code-related test failed."
        print("✅ Code Generation Test Passed!")

        print("\n🎉 ALL AI MODEL INFERENCE TESTS PASSED SUCCESSFULLY! 🎉\n")

    except AssertionError as error:
        print(f"❌ TEST FAILED: {error}")
    except Exception as e:
        print(f"⚠️ UNEXPECTED ERROR: {e}")

if __name__ == "__main__":
    test_model()