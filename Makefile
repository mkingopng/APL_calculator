# Clean existing build artifacts
.PHONY: clean
clean:
	rm -rf lambda_layer/python lambda_layer.zip lambda_package.zip package lambda-deployment.zip

# Build the Lambda Layer (Dependencies)
.PHONY: build-layer
build-layer: clean
	mkdir -p lambda_layer/python
	poetry export -f requirements.txt --output lambda_layer/requirements.txt --without-hashes
	pip install -r lambda_layer/requirements.txt -t lambda_layer/python
	cd lambda_layer && zip -r ../lambda_layer/python.zip python

# Package Flask app for Lambda
.PHONY: package-lambda
package-lambda:
	rm -rf package
	mkdir -p package
	cp -r flask_app lambda/lambda_handler.py package/
	cd package && zip -r ../lambda_package.zip .
	rm -rf package

# Deploy using AWS CDK
deploy: package-lambda
	cdk deploy --require-approval never

# run the Flask app locally
.PHONY: run-local
run-local:
	FLASK_APP=flask_app/flask_app.py FLASK_ENV=development flask run --host=0.0.0.0 --port=5000
