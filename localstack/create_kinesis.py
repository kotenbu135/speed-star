import boto3

client = boto3.client('kinesis', region_name='ap-northeast-1',
                      endpoint_url="http://localhost:4566",
                      aws_access_key_id="dummy",
                      aws_secret_access_key="dummy"
                      )

response = client.list_streams(
    ExclusiveStartStreamName='test'
)

print(response)
if not response['StreamNames']:
    client.create_stream(
        StreamName='test',
        StreamModeDetails={
            'StreamMode': 'ON_DEMAND'
        }
    )
