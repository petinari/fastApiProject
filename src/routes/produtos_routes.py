from typing import List

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.Schemas.produtos.schemas import ProdutoSchemaOut, ProdutoSchemaIn
from src.services import produtos_services

router = APIRouter(
    prefix="/produtos",
    tags=["produtos"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[ProdutoSchemaOut])
async def listar_produtos():
    return await produtos_services.listar_produtos()


@router.post('', response_model=ProdutoSchemaOut)
async def post_produto(produto: ProdutoSchemaIn = Body(...)):
    produto = jsonable_encoder(produto)
    return await produtos_services.adicionar_produto(produto)

