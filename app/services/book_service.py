from app.models.book import Book
from app.models.category import Category
from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import (
    BookCreate,
    BookUpdate
)


class BookService:

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(
        self,
        book_data: BookCreate
    ) -> Book:

        book = Book(
            title=book_data.title,
            isbn=book_data.isbn,
            published_year=book_data.published_year,
            author_id=book_data.author_id
        )

        return self.repository.create(book)

    def get_all_books(self) -> list[Book]:
        return self.repository.get_all()

    def get_book(
        self,
        book_id: int
    ) -> Book | None:

        return self.repository.get_by_id(book_id)

    def update_book(
        self,
        book_id: int,
        book_data: BookUpdate
    ) -> Book | None:

        book = self.repository.get_by_id(book_id)

        if book is None:
            return None

        book.title = book_data.title
        book.isbn = book_data.isbn
        book.published_year = book_data.published_year
        book.author_id = book_data.author_id

        return self.repository.update(book)

    def delete_book(
        self,
        book_id: int
    ) -> bool:

        book = self.repository.get_by_id(book_id)

        if book is None:
            return False

        self.repository.delete(book)

        return True

    def add_category(
        self,
        book_id: int,
        category_id: int
    ) -> Book | None:

        book = self.repository.get_by_id(book_id)

        if book is None:
            return None

        category = (
            self.repository.db.query(Category)
            .filter(Category.id == category_id)
            .first()
        )

        if category is None:
            return None

        existing_category = self.repository.get_category(
            book,
            category_id
        )

        if existing_category is not None:
            return book

        return self.repository.add_category(
            book,
            category
        )

    def remove_category(
        self,
        book_id: int,
        category_id: int
    ) -> Book | None:

        book = self.repository.get_by_id(book_id)

        if book is None:
            return None

        category = self.repository.get_category(
            book,
            category_id
        )

        if category is None:
            return None

        return self.repository.remove_category(
            book,
            category
        )