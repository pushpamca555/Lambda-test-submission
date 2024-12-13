# LambdaTest with Pytest

This project demonstrates how to run Selenium tests using `pytest` on LambdaTest.

## Prerequisites
1. Python 3.8+
2. LambdaTest account. Get your credentials from the [LambdaTest Dashboard](https://www.lambdatest.com/).

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your LambdaTest credentials to the `.env` file:
   ```plaintext
   LT_USERNAME=your_lambda_test_username
   LT_ACCESS_KEY=your_lambda_test_access_key
   ```

## Running Tests
Run all tests:
```bash
pytest
```

Run tests in parallel:
```bash
pytest -n 2
```

Generate an HTML report:
```bash
pytest --html=report.html --self-contained-html
```
