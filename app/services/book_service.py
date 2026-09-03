from app.models.book import Book
from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import (
    BookCreate,
    BookUpdate
)


class BookService:

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, book_data: BookCreate) -> Book:
        book = Book(
            title=book_data.title,
            isbn=book_data.isbn,
            published_year=book_data.published_year,
            author_id=book_data.author_id
        )

        return self.repository.create(book)

    def get_all_books(self) -> list[Book]:
        return self.repository.get_all()

    def get_book(self, book_id: int) -> Book | None:
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

    def delete_book(self, book_id: int) -> bool:
        book = self.repository.get_by_id(book_id)

        if book is None:
            return False

        self.repository.delete(book)

        return True