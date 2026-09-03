from app.models.category import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import (
    CategoryCreate,
    CategoryUpdate
)


class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def create_category(
        self,
        category_data: CategoryCreate
    ) -> Category:

        category = Category(
            name=category_data.name
        )

        return self.repository.create(category)

    def get_all_categories(self) -> list[Category]:
        return self.repository.get_all()

    def get_category(
        self,
        category_id: int
    ) -> Category | None:

        return self.repository.get_by_id(category_id)

    def update_category(
        self,
        category_id: int,
        category_data: CategoryUpdate
    ) -> Category | None:

        category = self.repository.get_by_id(category_id)

        if category is None:
            return None

        category.name = category_data.name

        return self.repository.update(category)

    def delete_category(
        self,
        category_id: int
    ) -> bool:

        category = self.repository.get_by_id(category_id)

        if category is None:
            return False

        self.repository.delete(category)

        return True