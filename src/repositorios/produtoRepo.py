from bson import ObjectId

from src.Schemas.schemas import ProdutoSchemaIn
from src.config.database import database


produtos_collection = database.get_collection("produtos_collection")


async def adicionar_produto(produto_data: ProdutoSchemaIn):
    produto = await produtos_collection.insert_one(produto_data)
    return await produtos_collection.find_one({"_id": produto.inserted_id})


async def listar_produtos():
    produtos = []
    async for produto in produtos_collection.find():
        produtos.append(produto)
    return produtos
