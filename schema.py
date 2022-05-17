from pydantic import BaseModel


class Req(BaseModel):
    text: str

    class Config:
        orm_mode = True


class IdToDel(BaseModel):
    id: int

    class Config:
        orm_mode = True
