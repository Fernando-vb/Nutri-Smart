import requests
import time

BASE_URL = "http://localhost:8000/api/v1"

def test_persistence():
    print("--- Starting Persistence Test ---")
    
    # 1. Initial State
    resp = requests.get(f"{BASE_URL}/dashboard/")
    initial_data = resp.json()
    initial_consumed = initial_data["caloriesConsumed"]
    print(f"Initial Consumed: {initial_consumed}", flush=True)

    # 2. Log Food
    print("Logging food (100 kcal)...", flush=True)
    requests.post(f"{BASE_URL}/food/log", json={"food_name": "Test Persistence", "calories": 100})

    # 3. Immediate Check
    resp = requests.get(f"{BASE_URL}/dashboard/")
    data_after_log = resp.json()
    consumed_after_log = data_after_log["caloriesConsumed"]
    print(f"Consumed after log: {consumed_after_log}", flush=True)
    print(f"Expected: {initial_consumed + 100}", flush=True)
    
    if consumed_after_log != initial_consumed + 100:
        print("FAILURE: Immediate update failed.", flush=True)
        return

    # 4. Wait and Check (Simulate user delay)
    print("Waiting 3 seconds...", flush=True)
    time.sleep(3)
    
    resp = requests.get(f"{BASE_URL}/dashboard/")
    final_data = resp.json()
    final_consumed = final_data["caloriesConsumed"]
    print(f"Final Consumed: {final_consumed}", flush=True)

    if final_consumed == consumed_after_log:
        print("SUCCESS: Data persisted.", flush=True)
    else:
        print(f"FAILURE: Data reset! Expected {consumed_after_log}, got {final_consumed}", flush=True)

if __name__ == "__main__":
    test_persistence()
