from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.author_repository import AuthorRepository
from app.schemas.author_schema import (
    AuthorCreate,
    AuthorResponse,
    AuthorUpdate
)
from app.services.author_service import AuthorService


router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)


def get_author_service(
    db: Session = Depends(get_db)
) -> AuthorService:

    repository = AuthorRepository(db)

    return AuthorService(repository)


@router.post(
    "",
    response_model=AuthorResponse,
    status_code=status.HTTP_201_CREATED
)
def create_author(
    author: AuthorCreate,
    service: AuthorService = Depends(get_author_service)
):
    return service.create_author(author)


@router.get(
    "",
    response_model=list[AuthorResponse]
)
def get_authors(
    service: AuthorService = Depends(get_author_service)
):
    return service.get_all_authors()


@router.get(
    "/{author_id}",
    response_model=AuthorResponse
)
def get_author(
    author_id: int,
    service: AuthorService = Depends(get_author_service)
):
    author = service.get_author(author_id)

    if author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found"
        )

    return author


@router.put(
    "/{author_id}",
    response_model=AuthorResponse
)
def update_author(
    author_id: int,
    author: AuthorUpdate,
    service: AuthorService = Depends(get_author_service)
):
    updated_author = service.update_author(
        author_id,
        author
    )

    if updated_author is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found"
        )

    return updated_author


@router.delete(
    "/{author_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_author(
    author_id: int,
    service: AuthorService = Depends(get_author_service)
):
    deleted = service.delete_author(author_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Author not found"
        )

    return None
