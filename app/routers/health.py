from fastapi import APIRouter

from app.schemas.status import Status
from app.service.kinesis import add_kinesis
from app.service.sqs import add_sqs

router = APIRouter()


@router.get("/")
async def health():
    return Status(status=200)


@router.get("/kinesis")
async def health():
    await add_kinesis()
    return Status(status=200)


@router.get("/sqs")
async def health():
    await add_sqs()
    return Status(status=200)
