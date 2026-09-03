from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    isbn: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )

    published_year: Mapped[int | None] = mapped_column(
        nullable=True
    )

    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id"),
        nullable=False
    )

    author: Mapped["Author"] = relationship(
        back_populates="books"
    )