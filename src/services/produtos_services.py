from src.repositorios.produto_repo import adicionar_produto, listar_produtos


async def add_produto(produto_schema_in):
    return await adicionar_produto(produto_schema_in)


async def get_produtos(produto_schema_in):
    return await listar_produtos(produto_schema_in)

