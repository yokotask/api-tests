# API Test Automation Framework

## 🚀 Overview
This is a **Pytest-based API test automation framework** for validating the `/simulate/` endpoint of the FastAPI simulation API. The framework includes **positive, edge, and negative test cases**, along with **Allure reporting** for detailed test execution insights.

## 📂 Project Structure
```
api-tests/
│── tests/
│   ├── test_positive.py      # Positive test cases
│   ├── test_edge_cases.py    # Edge case tests
│   ├── test_negative.py      # Negative test cases
│   ├── conftest.py           # Fixtures for reusable test data
│── requirements.txt          # Python dependencies
│── pytest.ini                # Pytest configuration
│── README.md                 # Documentation
```

## ✅ Setup Instructions
### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Run API Tests
```sh
pytest tests/ -v --alluredir=allure-results
```

### 3️⃣ View Allure Report
```sh
allure serve allure-results
```

### 4️⃣ Run Specific Test Categories
```sh
pytest tests/test_positive.py -v
pytest tests/test_edge_cases.py -v
pytest tests/test_negative.py -v
```

## 📌 Notes
- The framework supports **Pytest fixtures** for reusable test data.
- **Allure reporting** provides detailed insights into test execution.
- **CI/CD ready** with support for GitHub Actions.

🚀 **Happy Testing!**

