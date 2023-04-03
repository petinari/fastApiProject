from __future__ import annotations


from bson import ObjectId

from pydantic import BaseModel, Field

from src.utils.pyObjectId import PyObjectId


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class UsuarioSchema(OurBaseModel):
    nome: str
    senha: str


class ProdutoSchemaIn(OurBaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    descricao: str
    preco: float

    class Config:
        json_encoders = {ObjectId: str}


class ProdutoSchemaOut(OurBaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    descricao: str
    preco: float

    class Config:
        json_encoders = {ObjectId: str}


class PedidoSchema(OurBaseModel):
    usuario: UsuarioSchema
    quantidade: int
    endereco: str
    observacoes: str
