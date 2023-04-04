from fastapi.encoders import jsonable_encoder

from src.Schemas.produtos.schemas import ProdutoSchemaIn
from src.repositorios.produto_repo import ProdutoRepositorio


class ProdutoService:
    def __init__(self):
        pass

    async def add_produto(self, produto: ProdutoSchemaIn):
        return await ProdutoRepositorio().adicionar_produto(jsonable_encoder(produto))

    async def get_produtos(self):
        return await ProdutoRepositorio().listar_produtos()
