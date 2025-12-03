import os
from dotenv import load_dotenv
import google.generativeai as genai
import time

load_dotenv()

def find_working_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found.")
        return

    genai.configure(api_key=api_key)
    
    print("Listing models...")
    models = []
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                models.append(m.name)
    except Exception as e:
        print(f"ERROR listing models: {e}")
        return

    print(f"Found {len(models)} models: {models}")

    for model_name in models:
        print(f"\nTesting {model_name}...")
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("Hello, are you working?")
            with open("recommended_model.txt", "w") as f:
                f.write(model_name)
            print(f"RECOMMENDATION: {model_name}")
            return # Stop after finding the first working one
        except Exception as e:
            print(f"FAILED {model_name}: {e}")
            time.sleep(1) # Avoid hitting rate limits too hard during test

if __name__ == "__main__":
    find_working_model()
