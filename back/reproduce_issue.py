import requests
import time

BASE_URL = "http://localhost:8000/api/v1"

def test_sequential_updates():
    print("--- Starting Sequential Update Test ---")
    
    # 1. Initial State
    resp = requests.get(f"{BASE_URL}/dashboard/")
    initial_data = resp.json()
    initial_consumed = initial_data["caloriesConsumed"]
    print(f"Initial Consumed: {initial_consumed}")

    current_consumed = initial_consumed

    for i in range(1, 4):
        print(f"\n--- Iteration {i} ---")
        added_calories = 100
        print(f"Logging food ({added_calories} kcal)...")
        
        try:
            log_resp = requests.post(f"{BASE_URL}/food/log", json={"food_name": f"Test Food {i}", "calories": added_calories})
            if log_resp.status_code != 200:
                print(f"FAILURE: Log failed with status {log_resp.status_code}")
                print(log_resp.text)
                return
        except Exception as e:
            print(f"FAILURE: Exception during log: {e}")
            return

        # Immediate Check
        resp = requests.get(f"{BASE_URL}/dashboard/")
        data = resp.json()
        new_consumed = data["caloriesConsumed"]
        print(f"Consumed after log {i}: {new_consumed}")
        
        expected = current_consumed + added_calories
        if new_consumed == expected:
            print(f"SUCCESS: Iteration {i} updated correctly.")
            current_consumed = new_consumed
        else:
            print(f"FAILURE: Iteration {i} failed! Expected {expected}, got {new_consumed}")
            return

    print("\nAll iterations passed.")

if __name__ == "__main__":
    test_sequential_updates()
