from typing import Optional

from pydantic import BaseModel


class ShowCreate(BaseModel):
    title: str
    platform: Optional[str] = None
    poster_image_url: Optional[str] = None
    description: Optional[str] = None
    release_year: Optional[int] = None
    external_id: Optional[str] = None
    
class ShowResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    release_year: Optional[int] = None
    external_id: Optional[str] = None
    platform: Optional[str] = None
    poster_image_url: Optional[str] = None

    class Config:
        from_attributes = True