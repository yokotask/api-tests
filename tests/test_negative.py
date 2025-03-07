import requests

def test_missing_field(base_url, invalid_payload_missing_field):
    """Test request missing a required field"""
    response = requests.post(f"{base_url}/simulate/", json=invalid_payload_missing_field)
    assert response.status_code == 422, "Expected 422 Unprocessable Entity"

def test_wrong_data_type(base_url, invalid_payload_wrong_type):
    """Test request with incorrect data types"""
    response = requests.post(f"{base_url}/simulate/", json=invalid_payload_wrong_type)
    assert response.status_code == 422, "Expected 422 Unprocessable Entity"

def test_invalid_json(base_url):
    """Test API with completely invalid JSON format"""
    response = requests.post(f"{base_url}/simulate/", data="INVALID JSON")
    assert response.status_code == 422, "Expected 422 Unprocessable Entity"

def test_empty_request(base_url):
    """Test API with an empty request"""
    response = requests.post(f"{base_url}/simulate/", json={})
    assert response.status_code == 422, "Expected 422 Unprocessable Entity"

def test_missing_headers(base_url, valid_payload):
    """Test request without JSON headers"""
    response = requests.post(f"{base_url}/simulate/", data=str(valid_payload))
    assert response.status_code == 422, "Expected 422 Unprocessable Entity"
