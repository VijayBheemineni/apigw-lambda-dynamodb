import json
import boto3
import os
import logging
from decimal import Decimal


# Initialize the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb_table_name = os.environ.get('DYNAMODB_TABLE_NAME')


# Custom encoder to handle Decimal types.
# Added above class because we are getting below error.
"""
[ERROR] TypeError: Object of type Decimal is not JSON serializable
Traceback (most recent call last):
  File "/var/task/lambda_dynamodb.py", line 65, in lambda_handler
    "body": json.dumps(body),
  File "/var/lang/lib/python3.11/json/__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File "/var/lang/lib/python3.11/json/encoder.py", line 200, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/var/lang/lib/python3.11/json/encoder.py", line 258, in iterencode
    return _iterencode(o, 0)
  File "/var/lang/lib/python3.11/json/encoder.py", line 180, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
"""

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  # Or you can use str(obj) if you want to keep precision
        return super(DecimalEncoder, self).default(obj)

dynamodb = boto3.resource('dynamodb').Table(dynamodb_table_name)

def lambda_handler(event, context):
    logging.info(event)
    body = None
    status_code = 200
    headers = {
        "Content-Type": "application/json"
    }

    try:
        route_key = event.get('routeKey')      
        if route_key == "DELETE /employees/{id}":
            dynamodb.delete_item(
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = f"Deleted item {event['pathParameters']['id']}"
        elif route_key == "GET /employees/{id}":
            response = dynamodb.get_item(
                Key={
                    'id': event['pathParameters']['id']
                }
            )
            body = response.get('Item', {})
        elif route_key == "GET /employees":
            response = dynamodb.scan()
            body = response.get('Employees', [])
        elif route_key == "PUT /employees":
            request_json = json.loads(event['body'])
            dynamodb.put_item(
                Item={
                    'id': request_json['id'],
                    'name': request_json['name'],
                    'age': request_json['age'],
                }
            )
            body = f"Put item {request_json['id']}"  
        else:
            raise ValueError(f"Unsupported route: {route_key}")
    except Exception as err:
        status_code = 400
        body = str(err)
    return {
        "statusCode": status_code,
        "body": json.dumps(body, cls=DecimalEncoder),
        "headers": headers
    }
