import requests
import pytest

@pytest.mark.parametrize("i1, i2, a, b", [
    (0.0, 0.0, 0.0, 0.0),  # All values zero
    (-100.5, 200.2, -1.5, 3.8),  # Negative & positive mix
    (1e6, 1e6, 1e6, 1e6),  # Large numbers
    (1e-6, -1e-6, 1e-6, -1e-6),  # Small numbers close to zero
])
def test_edge_cases(base_url, i1, i2, a, b):
    """Test edge cases with extreme values"""
    payload = {
        "input_data": {"i1": i1, "i2": i2},
        "model_params": {"a": a, "b": b}
    }
    response = requests.post(f"{base_url}/simulate/", json=payload)

    assert response.status_code == 200, "Expected 200 OK"
    assert "outputs" in response.json()
