# cdk_app.py
"""

"""
import aws_cdk as cdk
from lib.flask_app_stack import FlaskAppStack

app = cdk.App()
FlaskAppStack(app, "FlaskAppStack")
app.synth()
