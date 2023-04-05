from typing import List

from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from src.Schemas.produtos.schemas import ProdutoSchemaOut, ProdutoSchemaIn
from src.services.produtos_services import ProdutoService
from src.utils.usuario.verifica_usuario_logado import verifica_usuario_logado

router = APIRouter(
    prefix="/produtos",
    tags=["produtos"],
    responses={404: {"description": "Not found"}},
)


@router.get("", dependencies=[Depends(verifica_usuario_logado)], response_model=List[ProdutoSchemaOut])
async def listar_produtos():
    return await ProdutoService().get_produtos_service()


@router.post("", dependencies=[Depends(verifica_usuario_logado)], response_model=ProdutoSchemaOut)
async def post_produto(produto: ProdutoSchemaIn = Body(...)):
    return await ProdutoService().add_produto_service(jsonable_encoder(produto))
