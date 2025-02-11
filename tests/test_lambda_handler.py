# tests/test_lambda_handler.py
"""
test lambda handler
"""
import sys
import os
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lambda_function.lambda_handler import handler

def test_lambda_valid_input():
    event = {
        "resource": "/{proxy+}",
        "path": "/api/v1/calculate",
        "httpMethod": "POST",
        "headers": {"Content-Type": "application/json"},
        "multiValueHeaders": {},
        "queryStringParameters": None,
        "multiValueQueryStringParameters": None,
        "requestContext": {
            "resourcePath": "/api/v1/calculate",
            "httpMethod": "POST",
            "path": "/api/v1/calculate",
        },
        "body": json.dumps({
            "body_weight": 80,
            "total_lifted": 600,
            "unit": "kg",
            "gender": "male",
            "competition": "CLPL",
            "age": 30
        }),
        "isBase64Encoded": False
    }
    response = handler(event, None)
    assert response["statusCode"] == 200
    assert "old_wilks" in json.loads(response["body"])

def test_lambda_invalid_input():
    event = {
        "resource": "/{proxy+}",
        "path": "/api/v1/calculate",
        "httpMethod": "POST",
        "headers": {"Content-Type": "application/json"},
        "multiValueHeaders": {},
        "queryStringParameters": None,
        "multiValueQueryStringParameters": None,
        "requestContext": {
            "resourcePath": "/api/v1/calculate",
            "httpMethod": "POST",
            "path": "/api/v1/calculate",
        },
        "body": json.dumps({}),  # Empty body should return 400
        "isBase64Encoded": False
    }
    response = handler(event, None)
    assert response["statusCode"] == 400

if __name__ == "__main__":
    pytest.main()
