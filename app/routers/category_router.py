from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate
)
from app.services.category_service import CategoryService


router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


def get_category_service(
    db: Session = Depends(get_db)
) -> CategoryService:

    repository = CategoryRepository(db)

    return CategoryService(repository)


@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_category(
    category: CategoryCreate,
    service: CategoryService = Depends(get_category_service)
):
    return service.create_category(category)


@router.get(
    "",
    response_model=list[CategoryResponse]
)
def get_categories(
    service: CategoryService = Depends(get_category_service)
):
    return service.get_all_categories()


@router.get(
    "/{category_id}",
    response_model=CategoryResponse
)
def get_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service)
):
    category = service.get_category(category_id)

    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )

    return category


@router.put(
    "/{category_id}",
    response_model=CategoryResponse
)
def update_category(
    category_id: int,
    category: CategoryUpdate,
    service: CategoryService = Depends(get_category_service)
):
    updated_category = service.update_category(
        category_id,
        category
    )

    if updated_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )

    return updated_category


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_category(
    category_id: int,
    service: CategoryService = Depends(get_category_service)
):
    deleted = service.delete_category(category_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )

    return None