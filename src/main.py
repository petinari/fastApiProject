from fastapi import FastAPI

from src.routes import produtos_routes, usuarios_routes

app = FastAPI()
app.include_router(produtos_routes.router)
app.include_router(usuarios_routes.router)