from sqlalchemy.orm import Session

from conexion import comprobar_conexion
from configuracion import engine
from consultas import listar_libros, buscar_libro_por_id

def main():
    comprobar_conexion()

    with Session(engine) as session:
        libros = listar_libros(session)
        print("\n -------LISTAR LIBROS")
        for libro in libros:
            print(libro)

        print("\n --------BUSCAR LIBRO POR ID")
        libro = buscar_libro_por_id(session, 1)
        print(libro)
        print("\n --------BUSCAR LIBRO POR ID (inexistente)")
        libro_2 = buscar_libro_por_id(session, 1000000)
        print(libro_2)


if __name__ == "__main__":
    main()