from src.Schemas.produtos.schemas import ProdutoSchemaIn
from src.config.database import database


class ProdutoRepositorio:
    def __init__(self):
        self.produtos_collection = database.get_collection("produtos_collection")

    async def adicionar_produto_repo(self, produto_schema_in: ProdutoSchemaIn):
        produto = await self.produtos_collection.insert_one(produto_schema_in)
        return await self.produtos_collection.find_one({"_id": produto.inserted_id})

    async def listar_produtos_repo(self):
        produtos = []
        async for produto in self.produtos_collection.find():
            produtos.append(produto)
        return produtos
