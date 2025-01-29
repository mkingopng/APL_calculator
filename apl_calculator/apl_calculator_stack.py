# lib/flask_app_stack.py
"""
cdk stack to deploy calculator app
"""
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_iam as iam,
)
from constructs import Construct

class FlaskAppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define an IAM Role for Lambda
        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # Define Lambda function for Flask app
        flask_lambda = _lambda.Function(
            self, "FlaskLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,  # Ensure your Python version matches
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset("../APL_calculator"),  # Adjust if needed
            role=lambda_role,
            memory_size=512,
            timeout=Stack.of(self).to_duration(30)  # 30 seconds timeout
        )

        # Define API Gateway to expose Lambda function
        api = apigw.LambdaRestApi(
            self, "FlaskApiGateway",
            handler=flask_lambda,
            proxy=True
        )

        # Output API Gateway URL
        self.api_url = api.url
