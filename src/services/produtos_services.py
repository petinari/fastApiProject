from fastapi.encoders import jsonable_encoder

from src.Schemas.produtos.schemas import ProdutoSchemaIn
from src.repositorios.produto_repo import ProdutoRepositorio


class ProdutoService:
    def __init__(self):
        pass

    async def add_produto_service(self, produto: ProdutoSchemaIn):
        return await ProdutoRepositorio().adicionar_produto_repo(jsonable_encoder(produto))

    async def get_produtos_service(self):
        return await ProdutoRepositorio().listar_produtos_repo()
