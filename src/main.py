import string
from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette import status

from src.Schemas.schemas import ProdutoSchemaIn, ProdutoSchemaOut
from fastapi import FastAPI, Body

from src.repositorios.produtoRepo import adicionar_produto, listar_produtos
from src.routes import produtosRoutes

app = FastAPI()
app.include_router(produtosRoutes.router)

"""@app.post('/produto', status_code=status.HTTP_201_CREATED, response_model=ProdutoSchemaOut)
async def post_produto(produto: ProdutoSchemaIn = Body(...)):
    produto = jsonable_encoder(produto)
    ProdutoSchemaOut = await adicionar_produto(produto)
    return ProdutoSchemaOut


@app.get('/produtos', response_model=List[ProdutoSchemaOut])
async def get_produtos():
    return await listar_produtos()
"""