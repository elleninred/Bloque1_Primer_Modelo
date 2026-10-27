
from decimal import Decimal
from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


# Clase Libro con constructor repr
class Libro(Base):
    __tablename__ = "libros"

    id_libro: Mapped[int] = mapped_column(
        primary_key=True
    )

    isbn: Mapped[str] = mapped_column(
        String(20),
        unique=True
    )

    titulo: Mapped[str] = mapped_column(
        String(200)
    )

    precio: Mapped[Decimal] = mapped_column(
        Numeric(10, 2)
    )

    def __repr__(self) -> str:
        return f"Libro(id={self.id_libro}, titulo={self.titulo!r}, precio={self.precio})"

