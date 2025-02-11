# tests/test_flask_app_stack.py
"""
Test the apl_calculator stack.
"""
import aws_cdk as core
from aws_cdk import assertions
from lib.flask_app_stack import FlaskAppStack


def test_sqs_queue_created():
    app = core.App()
    stack = FlaskAppStack(app, "apl-calculator")
    template = assertions.Template.from_stack(stack)

