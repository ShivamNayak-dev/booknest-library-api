from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    bio: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )