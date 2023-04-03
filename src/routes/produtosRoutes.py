from typing import List

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.Schemas.schemas import ProdutoSchemaOut, ProdutoSchemaIn
from src.services import produtosServices

router = APIRouter(
    prefix="/produtos",
    tags=["produtos"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[ProdutoSchemaOut])
async def listar_produtos():
    return await produtosServices.listar_produtos()


@router.post('', response_model=ProdutoSchemaOut)
async def post_produto(produto: ProdutoSchemaIn = Body(...)):
    produto = jsonable_encoder(produto)
    return await produtosServices.adicionar_produto(produto)

