import boto3
import os
from boto3.dynamodb.conditions import Key

# Hola a todos, hoy es 16 de marzo, el profe cumple anos el 29 de marzo

DYNAMO_BD = os.environ['DYNAMO_BD']

class DynamoAccessor:
    def __init__(self, dynamo_table):
        dynamo_db = boto3.resource('dynamodb')
        self.table = dynamo_db.Table(dynamo_table)

    def get_data_from_dynamo(self, cc):
        response = self.table.query(KeyConditionExpression=Key('cc').eq(cc))
        return response["Items"][0] if any(response["Items"]) else None

def lambda_handler(event, context):
    dynamo_backend = DynamoAccessor(DYNAMO_BD)
    db_element = dynamo_backend.get_data_from_dynamo(event['cc'])
    return db_element

