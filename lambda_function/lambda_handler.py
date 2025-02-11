# lambda_function/lambda_handler.py
"""
lambda_function handler
"""
from flask_app.flask_app import app
from mangum import Mangum

handler = Mangum(app)
