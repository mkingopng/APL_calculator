# lambda/lambda_handler.py
"""
lambda handler
"""
from flask_app import app  # Import your Flask app
from mangum import Mangum  # AWS Lambda + Flask adapter

handler = Mangum(app)  # Convert Flask app into a Lambda handler
