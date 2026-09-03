from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import (
    BookCreate,
    BookResponse,
    BookUpdate
)
from app.services.book_service import BookService


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


def get_book_service(
    db: Session = Depends(get_db)
) -> BookService:

    repository = BookRepository(db)

    return BookService(repository)


@router.post(
    "",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    book: BookCreate,
    service: BookService = Depends(get_book_service)
):
    return service.create_book(book)


@router.get(
    "",
    response_model=list[BookResponse]
)
def get_books(
    service: BookService = Depends(get_book_service)
):
    return service.get_all_books()


@router.post(
    "/{book_id}/categories/{category_id}",
    response_model=BookResponse
)
def add_category_to_book(
    book_id: int,
    category_id: int,
    service: BookService = Depends(get_book_service)
):
    book = service.add_category(
        book_id,
        category_id
    )

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book or category not found"
        )

    return book


@router.delete(
    "/{book_id}/categories/{category_id}",
    response_model=BookResponse
)
def remove_category_from_book(
    book_id: int,
    category_id: int,
    service: BookService = Depends(get_book_service)
):
    book = service.remove_category(
        book_id,
        category_id
    )

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book or category not found"
        )

    return book


@router.get(
    "/{book_id}",
    response_model=BookResponse
)
def get_book(
    book_id: int,
    service: BookService = Depends(get_book_service)
):
    book = service.get_book(book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


@router.put(
    "/{book_id}",
    response_model=BookResponse
)
def update_book(
    book_id: int,
    book: BookUpdate,
    service: BookService = Depends(get_book_service)
):
    updated_book = service.update_book(
        book_id,
        book
    )

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return updated_book


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_book(
    book_id: int,
    service: BookService = Depends(get_book_service)
):
    deleted = service.delete_book(book_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return None