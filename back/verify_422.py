import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_invalid_email():
    email = "notanemail"
    password = "password123"
    name = "Invalid User"

    print(f"Registering user with invalid email: {email}")
    resp = requests.post(f"{BASE_URL}/auth/register", json={"email": email, "password": password, "name": name})
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")

if __name__ == "__main__":
    test_invalid_email()
