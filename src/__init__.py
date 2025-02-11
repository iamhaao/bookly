from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Bookly",
    version=version,
    description="A REST API for a book review web service"
)

app.include_router(book_router,prefix='/api/{version}/books', tags=['Books'])