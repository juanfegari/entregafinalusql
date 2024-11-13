import sqlite3
from lexer_USQLaSQL import *
from FluentApiSQL import *

def crear_base_de_datos():
    """
    Esta función crea la base de datos y la tabla en donde se encuentran los datos a trabajar.
    """
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        ciudad TEXT NOT NULL
    );
    ''')

    cursor.execute("INSERT INTO usuarios (nombre, edad, ciudad) VALUES ('Juan', 25, 'Madrid')")
    cursor.execute("INSERT INTO usuarios (nombre, edad, ciudad) VALUES ('Ana', 22, 'Barcelona')")
    cursor.execute("INSERT INTO usuarios (nombre, edad, ciudad) VALUES ('Luis', 30, 'Madrid')")
    cursor.execute("INSERT INTO usuarios (nombre, edad, ciudad) VALUES ('María', 28, 'Valencia')")

    conn.commit()
    conn.close()
    print("\n Base de datos y tabla creadas con datos de ejemplo. \n")


def probar_traductor_y_api():
    """
    Esta función testea el traductor SQL y la API Fluent
    """
    consulta_usql = "TRAEME TODO DE_LA_TABLA usuarios DONDE edad > 18;"
    print("Consulta USQL: ", consulta_usql)
    resultado = traducir_usql_a_sql(consulta_usql)
    print("\nConsulta SQL traducida:", resultado)

    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    cursor.execute(resultado)
    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

    conn.close()

if __name__ == '__main__':
    crear_base_de_datos()  
    probar_traductor_y_api()  
