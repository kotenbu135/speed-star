from aiobotocore.session import get_session


async def add_kinesis():
    session = get_session()
    async with session.create_client('kinesis',
                                     region_name='ap-northeast-1',
                                     endpoint_url="http://localstack:4566",
                                     aws_secret_access_key="dummy",
                                     aws_access_key_id="dummy"
                                     ) as aio_kinesis:
        await aio_kinesis.put_record(
            StreamName='test',
            Data=b'bytes',
            PartitionKey="123"
        )
