from pydantic import BaseModel, Field
from typing import List, Optional

class MovieDetailResponseSchema(BaseModel):
    id: int
    name: str
    date: Optional[str] = None
    score: float
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: int
    revenue: int
    country: str

    class Config:
        orm_mode = True
        from_attributes = True

class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailResponseSchema]
    prev_page: Optional[str] = None
    next_page: Optional[str] = None
    total_pages: int
    total_items: int
