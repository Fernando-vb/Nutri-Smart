import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_calorie_update():
    print("Logging food...")
    try:
        log_resp = requests.post(f"{BASE_URL}/food/log", json={"food_name": "Test Food", "calories": 500})
        print(f"Status: {log_resp.status_code}")
        print(f"Text: {log_resp.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_calorie_update()
