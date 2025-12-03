import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def list_models():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found.")
        return

    genai.configure(api_key=api_key)
    
    print("Available models for generateContent:")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f" - {m.name}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    list_models()
