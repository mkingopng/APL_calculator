# lib/flask_app_stack.py
"""
CDK code for infrastructure to deploy calculator app
"""
import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_certificatemanager as acm,
    aws_route53 as route53,
    aws_route53_targets as targets,
)

class FlaskAppStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):  # ✅ Use constructs.Construct
        super().__init__(scope, id, **kwargs)

        # ✅ Fetch your existing certificate in ACM
        certificate_arn = ""  # fixme: insert real certificate ARN
        certificate = acm.Certificate.from_certificate_arn(self, "Certificate", certificate_arn)

        flask_lambda_layer = _lambda.LayerVersion(
            self, "FlaskLambdaLayer",
            code=_lambda.Code.from_asset("lambda_layer/python.zip"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_10],
            description="Layer for Flask dependencies"
        )

        flask_lambda = _lambda.Function(
            self, "FlaskLambda",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset(".", exclude=["cdk.out", ".git", "venv", "__pycache__"]),
            memory_size=512,
            timeout=cdk.Duration.seconds(30),
            layers=[flask_lambda_layer],
        )

        # ✅ Create API Gateway with Custom Domain
        api = apigw.RestApi(
            self, "FlaskApiGateway",
            rest_api_name="Flask API Gateway",
            domain_name=apigw.DomainNameOptions(
                domain_name="api.michaelkingston.com.au",
                certificate=certificate
            )
        )

        # ✅ Add a proxy integration to forward all requests to Lambda
        api.root.add_proxy(
            default_integration=apigw.LambdaIntegration(flask_lambda),
            any_method=True
        )

        # ✅ Create a Route53 A Record (if needed)
        hosted_zone = route53.HostedZone.from_lookup(self, "HostedZone", domain_name="michaelkingston.com.au")
        route53.ARecord(
            self, "ApiARecord",
            record_name="api",
            zone=hosted_zone,
            target=route53.RecordTarget.from_alias(targets.ApiGateway(api))
        )