from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    title: str
    isbn: str
    published_year: int | None = None
    author_id: int


class BookUpdate(BaseModel):
    title: str
    isbn: str
    published_year: int | None = None
    author_id: int


class BookResponse(BaseModel):
    id: int
    title: str
    isbn: str
    published_year: int | None = None
    author_id: int

    model_config = ConfigDict(from_attributes=True)