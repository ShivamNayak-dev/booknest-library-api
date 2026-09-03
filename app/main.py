from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.author import Author
from app.routers.author_router import router as author_router
from app.routers.book_router import router as book_router

from app.models.book import Book


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="BookNest Library Management API",
    description=(
        "A Library Management REST API built with "
        "FastAPI, SQLAlchemy, and MySQL."
    ),
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to BookNest Library Management API"
    }


@app.get("/about")
def about():
    return {
        "message": (
            "BookNest is a Library Management API "
            "built with FastAPI"
        )
    }


app.include_router(author_router)
app.include_router(book_router)