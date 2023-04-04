from __future__ import annotations

from bson import ObjectId
from pydantic import Field

from src.Schemas.base_model_app import BaseModelApp
from src.utils.pyObjectId import PyObjectId


class ProdutoSchemaIn(BaseModelApp):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    descricao: str
    preco: float


class ProdutoSchemaOut(BaseModelApp):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    descricao: str
    preco: float

    class Config:
        json_encoders = {ObjectId: str}
