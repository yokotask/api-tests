import requests
import allure

@allure.epic("API Testing")
@allure.feature("Positive Test Cases")
@allure.story("Valid Simulation Request")
@allure.description("Test that API returns 200 OK with correct inputs")
def test_valid_request(base_url, valid_payload):
    """Test valid input values"""
    response = requests.post(f"{base_url}/simulate/", json=valid_payload)

    assert response.status_code == 200, "Expected 200 OK"

    json_data = response.json()
    assert "outputs" in json_data, "Response missing 'outputs'"
    assert isinstance(json_data["outputs"]["o1"], float)
    assert isinstance(json_data["outputs"]["o2"], float)
    assert isinstance(json_data["outputs"]["o3"], float)

@allure.story("Valid Request with Different Values")
@allure.description("Test API with a different valid set of values")
def test_valid_different_values(base_url):
    """Test API with a different valid set of values"""
    payload = {
        "input_data": {"i1": 10.5, "i2": -7.2},
        "model_params": {"a": 3.1, "b": -1.8}
    }
    response = requests.post(f"{base_url}/simulate/", json=payload)

    assert response.status_code == 200, "Expected 200 OK"
    assert "outputs" in response.json()
