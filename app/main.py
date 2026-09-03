from fastapi import FastAPI

from app.database.database import engine


app = FastAPI(
    title="BookNest Library Management API",
    description="A Library Management REST API built with FastAPI, SQLAlchemy, and MySQL.",
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
        "message": "BookNest is a Library Management API built with FastAPI"
    }


@app.get("/test-db")
def test_database():
    with engine.connect() as connection:
        return {
            "message": "Database connection successful"
        }