from pydantic import BaseModel

class AreaCreate(BaseModel):
    name: str
    hospitals: int
    pharmacies: int
    libraries: int
    playgrounds: int
    gyms: int

class AreaResponse(BaseModel):
    id: int
    name: str
    hospitals: int
    pharmacies: int
    libraries: int
    playgrounds: int
    gyms: int
    score: float

    class Config:
        from_attributes = True