import sqlite3
miConexion = sqlite3.connect('segundaBase')
miCursor = miConexion.cursor()

#miCursor.execute('''
    #CREATE TABLE PRODUCTOS(
    #    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    #    PRECIO INTEGER,
    #    SECCION VARCHAR(50)
    #)
#''')

productos = [
    ("Balon",8,"Deportes"),
    ("Camisa",12,"Ropa"),
    ("Celular",80,"Tecnologia")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 2")

miCursor.execute("SELECT * FROM PRODUCTOS")
datos = miCursor.fetchall()

for dato in datos:
    print(dato)
miConexion.commit()
miConexion.close()