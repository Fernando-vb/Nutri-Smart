import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

models_to_test = [
    "gemini-3-pro-image-preview",
    "nano-banana-pro-preview",
    "gemini-robotics-er-1.5-preview",
    "gemini-2.5-computer-use-preview-10-2025",
    "gemini-1.5-flash"
]

print("Testing models...")
for model_name in models_to_test:
    print(f"Testing {model_name}...")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print(f"SUCCESS: {model_name} worked!")
        break
    except Exception as e:
        error_msg = str(e).split('\n')[0] # Keep it short
        print(f"FAILED: {model_name} - {error_msg}")
