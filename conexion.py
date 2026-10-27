from sqlalchemy import text

from configuracion import engine

#crear engine

def comprobar_conexion():
    with engine.connect() as conexion:
        resultado = conexion.execute(
            text("SELECT current_database(), current_user")
        )
        print(resultado.one())
