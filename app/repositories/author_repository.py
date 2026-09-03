from sqlalchemy.orm import Session

from app.models.author import Author


class AuthorRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, author: Author) -> Author:
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)

        return author

    def get_all(self) -> list[Author]:
        return self.db.query(Author).all()

    def get_by_id(self, author_id: int) -> Author | None:
        return (
            self.db.query(Author)
            .filter(Author.id == author_id)
            .first()
        )

    def update(self, author: Author) -> Author:
        self.db.commit()
        self.db.refresh(author)

        return author

    def delete(self, author: Author) -> None:
        self.db.delete(author)
        self.db.commit()