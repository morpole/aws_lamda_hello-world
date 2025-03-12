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
1. **Create an AWS Lambda Function**:
   - Go to the AWS Lambda Console.
   - Click "Create function" and choose "Author from scratch".
   - Name: `HelloWorld`.
   - Runtime: Python 3.9 (or the latest available).
   - Click "Create function".

2. **Upload the Code**:
   - Copy the contents of `lambda_function.py` from this repository.
   - In the Lambda console, paste the code into the editor and click "Deploy".

3. **Add an API Gateway Trigger**:
   - In the Lambda console, go to "Function overview".
   - Click "Add trigger" and select "API Gateway".
   - Choose "Create a new API" and set it to "HTTP API" (open security for this demo).
   - Click "Add" to create the trigger.
   - Note the API endpoint URL (e.g., `https://abc123.execute-api.us-east-1.amazonaws.com/default/HelloWorld`).

## Usage
- **Access the Endpoint**:
  - Use the API Gateway URL with a `name` query parameter:
    ```
    https://abc123.execute-api.us-east-1.amazonaws.com/default/HelloWorld?name=Alex
    ```
    Response: `Hello, Alex!`
  - Without a `name` parameter, it defaults to:
    ```
    https://abc123.execute-api.us-east-1.amazonaws.com/default/HelloWorld
    ```
    Response: `Hello, World!`

- **View Logs**:
  - Go to the Lambda console > "Monitor" tab > "View logs in CloudWatch".
  - Open the log group `/aws/lambda/HelloWorld` and check the latest log stream.
  - Logs show the incoming event and processed name, e.g.:
    ```
    Received event: {'queryStringParameters': {'name': 'Alex'}, ...}
    Processing name: Alex
    ```

## Code Explanation
- **File**: `lambda_function.py`
- **Functionality**:
  - Extracts the `name` from the `queryStringParameters` of the incoming event.
  - Logs the event and name to CloudWatch.
  - Returns a plain-text response with a personalized greeting.

## Learning Outcomes
This project demonstrates:
- Creating and deploying a serverless function with AWS Lambda.
- Setting up an HTTP endpoint using API Gateway.
- Logging and monitoring with CloudWatch.
- Basic Git and GitHub usage for version control.



