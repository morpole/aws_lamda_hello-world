# AWS Lambda Hello World

A simple serverless application built with AWS Lambda and API Gateway. This project demonstrates a basic Lambda function that responds with a personalized greeting ("Hello, [Your Name]!") when triggered via an HTTP endpoint. It also logs events to Amazon CloudWatch for debugging and monitoring.

## Features
- **Serverless Function**: Uses AWS Lambda to run a Python function without managing servers.
- **HTTP Trigger**: Integrated with API Gateway to create a public HTTP endpoint.
- **Personalized Response**: Accepts a `name` query parameter to customize the greeting (e.g., `?name=Alex`).
- **Logging**: Logs incoming events and processed names to CloudWatch Logs for monitoring.

## Prerequisites
- An AWS account with access to Lambda, API Gateway, and CloudWatch.
- Basic knowledge of Python and AWS services.
- Git installed to clone this repository.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/morpole/aws_lambda_hello-world.git
   cd aws_lambda_hello-world# aws_lamda-hello-world
A simple AWS Lambda function with API Gateway trigger.

