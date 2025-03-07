import pytest

@pytest.fixture
def valid_payload():
    """Valid payload for a successful request"""
    return {
        "input_data": {"i1": 2.0, "i2": 3.0},
        "model_params": {"a": 1.5, "b": 2.0}
    }

@pytest.fixture
def invalid_payload_missing_field():
    """Payload missing a required field (i2)"""
    return {
        "input_data": {"i1": 2.0},  # Missing "i2"
        "model_params": {"a": 1.5, "b": 2.0}
    }

@pytest.fixture
def invalid_payload_wrong_type():
    """Payload with incorrect data type"""
    return {
        "input_data": {"i1": "text", "i2": 3.0},  # "i1" should be a float
        "model_params": {"a": 1.5, "b": 2.0}
    }

@pytest.fixture
def base_url():
    """Base API URL fixture"""
    return "http://127.0.0.1:8000"
