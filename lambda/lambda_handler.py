# lambda/lambda_handler.py
"""
lambda handler
"""
from flask_app.flask_app import app
from mangum import Mangum

handler = Mangum(app)
