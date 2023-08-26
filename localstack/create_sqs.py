import boto3

client = boto3.client('sqs', region_name='ap-northeast-1',
                      endpoint_url="http://localhost:4566",
                      aws_access_key_id="dummy",
                      aws_secret_access_key="dummy"
                      )

response = client.list_queues(
    QueueNamePrefix='test'
)

print(response)
if not response['QueueUrls']:
    client.create_queue(
        QueueName='test'
    )
