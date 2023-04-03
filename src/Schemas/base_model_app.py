
from typing import Any
from bson import ObjectId
from pydantic import BaseModel

from src.utils.pyObjectId import PyObjectId


class BaseModelApp(BaseModel):
     class Config:
        orm_mode = True
        json_encoders = {ObjectId: str}
   


class PyObjectId(PyObjectId): 
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
    
   
