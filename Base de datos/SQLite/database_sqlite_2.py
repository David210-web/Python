import sqlite3

miConexion = sqlite3.connect('gestionProductos')
miCursor = miConexion.cursor()

#miCursor.execute('''
    #CREATE TABLE PRODUCTOS(
    #    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    #    NOMBRE_ARTICULO VARCHAR(50),
    #    PRECIO INTEGER,
    #    SECCION VARCHAR(20)
    #)
#''')

productos = [
    ("Pelota",20,"Jugueteria"),
    ("Pantalon",45,"Confeccion"),
    ("Jarron",45,"Ceramica")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)
miCursor.execute("SELECT * FROM PRODUCTOS")
datos = miCursor.fetchall()

for dato in datos:
    print(dato)

miConexion.commit()
miConexion.close()