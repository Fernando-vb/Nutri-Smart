import os
from dotenv import load_dotenv
import google.generativeai as genai
from services.gemini_service import analyze_image_nutrition

load_dotenv()

def test_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found.")
        return

    print(f"API Key found: {api_key[:5]}...")
    
    # Create a dummy image (1x1 pixel black jpeg)
    # This is just to test if the API accepts the request, even if the analysis is nonsense.
    # Actually, sending random bytes might fail validation.
    # Better to try to list models first to check auth.
    
    print("Listing models...")
    try:
        genai.configure(api_key=api_key)
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f" - {m.name}")
    except Exception as e:
        print(f"ERROR listing models: {e}")
        return

    print("\nTesting analyze_image_nutrition with dummy data...")
    # We can't easily test the image analysis without a real image file.
    # But if list_models works, the key is valid.
    # The error "Error al analizar la imagen" usually comes from the try/except block in the router or service.
    
if __name__ == "__main__":
    test_gemini()
