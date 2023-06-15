import boto3
import botocore.session
import random

array_indexes = ["1", "2", "3", "4"]

valor_aleatorio = random.choice(array_indexes)

client = boto3.client("dynamodb",
  region_name="us-east-1",
  endpoint_url="http://localhost.localstack.cloud:4566/",
)

response = client.get_item(
    TableName='Dicas',
    Key={
        'Id': {'N': valor_aleatorio}
        }
    )

print("Dica do dia: ", response['Item']['Dica'])
