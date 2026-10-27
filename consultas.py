from sqlalchemy import select
from sqlalchemy.orm import Session

from modelos import Libro


#Funciones
def listar_libros(session: Session):
    consulta = select(Libro).order_by(Libro.titulo)
    return session.scalars(consulta).all()

def buscar_libro_por_id(session: Session, id_libro: int) -> Libro | None:
    return session.get(Libro, id_libro)