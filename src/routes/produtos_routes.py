from typing import List

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from src.Schemas.produtos.schemas import ProdutoSchemaOut, ProdutoSchemaIn
from src.services.produtos_services import ProdutoService

router = APIRouter(
    prefix="/produtos",
    tags=["produtos"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[ProdutoSchemaOut])
async def listar_produtos():
    return await ProdutoService().get_produtos()


@router.post("", response_model=ProdutoSchemaOut)
async def post_produto(produto: ProdutoSchemaIn = Body(...)):
    return await ProdutoService().add_produto(jsonable_encoder(produto))
