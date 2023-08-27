import boto3

client = boto3.client('sqs', region_name='ap-northeast-1',
                      endpoint_url="http://localhost:4566",
                      aws_access_key_id="dummy",
                      aws_secret_access_key="dummy"
                      )

client.create_queue(
    QueueName='test'
)
