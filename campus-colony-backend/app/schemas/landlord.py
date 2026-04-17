from pydantic import BaseModel

class LandlordCreate(BaseModel):
    name: str
    phone: str
    email: str | None = None

class LandlordResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str | None

    class Config:
        orm_mode = True