from pydantic import BaseModel


class Status(BaseModel):
    status: int
