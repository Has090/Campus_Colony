from pydantic import BaseModel, Field
from datetime import datetime


class ReviewCreate(BaseModel):
    content: str = Field(..., min_length=1, max_length=500)
    rating: int = Field(..., ge=1, le=5)



class ReviewUpdate(BaseModel):
    content: str | None = Field(None, min_length=1, max_length=500)
    rating: int | None = Field(None, ge=1, le=5)


class ReviewResponse(BaseModel):
    id: int
    content: str
    rating: int
    user_id: int
    listing_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ListingReviewResponse(BaseModel):
    average_rating: float
    total_reviews: int
    reviews: list[ReviewResponse]