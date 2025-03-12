def lambda_handler(event, context):
    print(f"Received event: {event}")  # Log the entire event
    name = event.get('queryStringParameters', {}).get('name', 'World')
    print(f"Processing name: {name}")  # Log the name being used
    return {
        'statusCode': 200,
        'body': f"Hello, {name}!",
        'headers': {'Content-Type': 'text/plain'}
    }