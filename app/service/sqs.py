from aiobotocore.session import get_session


async def add_sqs():
    session = get_session()
    async with session.create_client('sqs',
                                     region_name='ap-northeast-1',
                                     endpoint_url="http://localhost:4566",
                                     aws_secret_access_key="dummy",
                                     aws_access_key_id="dummy"
                                     ) as aio_sqs:
        await aio_sqs.send_message(
            QueueUrl='test',
            MessageBody='string',
        )
