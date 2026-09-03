from fastapi import FastAPI


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


# uvicorn app.main:app --reload