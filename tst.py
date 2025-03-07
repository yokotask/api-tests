import requests

BASE_URL = "http://127.0.0.1:8000"

# Correct JSON structure with nested parameters
payload = {
    "input_data": {"i1": 2.0, "i2": 3.0},
    "model_params": {"a": 1.5, "b": 2.0}
}

response = requests.post(f"{BASE_URL}/simulate/", json=payload)

print(response.status_code)  # Should be 200
print(response.json())       # Check API response
