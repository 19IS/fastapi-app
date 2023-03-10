from datetime import datetime
from typing import List

from bson.objectid import ObjectId
from pydantic import BaseModel


class NewsBaseSchema(BaseModel):
    title: str
    content: str
    image: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CreateNewsSchema(NewsBaseSchema):
    pass


class NewsResponse(NewsBaseSchema):
    id: str
    created_at: datetime
    updated_at: datetime


class UpdateNewsSchema(BaseModel):
    title: str | None = None
    image: str | None = None
    content: str | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ListNewsResponse(BaseModel):
    status: str
    results: int
    posts: List[NewsBaseSchema]
