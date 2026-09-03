from app.models.author import Author
from app.repositories.author_repository import AuthorRepository
from app.schemas.author_schema import (
    AuthorCreate,
    AuthorUpdate
)


class AuthorService:

    def __init__(self, repository: AuthorRepository):
        self.repository = repository

    def create_author(self, author_data: AuthorCreate) -> Author:
        author = Author(
            name=author_data.name,
            bio=author_data.bio
        )

        return self.repository.create(author)

    def get_all_authors(self) -> list[Author]:
        return self.repository.get_all()

    def get_author(self, author_id: int) -> Author | None:
        return self.repository.get_by_id(author_id)

    def update_author(
        self,
        author_id: int,
        author_data: AuthorUpdate
    ) -> Author | None:

        author = self.repository.get_by_id(author_id)

        if author is None:
            return None

        author.name = author_data.name
        author.bio = author_data.bio

        return self.repository.update(author)

    def delete_author(self, author_id: int) -> bool:
        author = self.repository.get_by_id(author_id)

        if author is None:
            return False

        self.repository.delete(author)

        return True