from sqlalchemy.orm import Session

from app.models.book import Book
from app.models.category import Category


class BookRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, book: Book) -> Book:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)

        return book

    def get_all(self) -> list[Book]:
        return self.db.query(Book).all()

    def get_by_id(self, book_id: int) -> Book | None:
        return (
            self.db.query(Book)
            .filter(Book.id == book_id)
            .first()
        )

    def update(self, book: Book) -> Book:
        self.db.commit()
        self.db.refresh(book)

        return book

    def delete(self, book: Book) -> None:
        self.db.delete(book)
        self.db.commit()

    def get_category(
        self,
        book: Book,
        category_id: int
    ) -> Category | None:

        return next(
            (
                category
                for category in book.categories
                if category.id == category_id
            ),
            None
        )

    def add_category(
        self,
        book: Book,
        category: Category
    ) -> Book:

        book.categories.append(category)

        self.db.commit()
        self.db.refresh(book)

        return book

    def remove_category(
        self,
        book: Book,
        category: Category
    ) -> Book:

        book.categories.remove(category)

        self.db.commit()
        self.db.refresh(book)

        return book