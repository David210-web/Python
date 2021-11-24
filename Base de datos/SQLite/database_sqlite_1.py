#Bases de datos sqlite

#Pasos a seguir
#1-Abrir - Crear conexion
#2-Crear puntero o cursor(nos sirve para crear Querys y manejar resultados)
#3-Ejecutar query (consulta) SQL (con el puntero)
#4-Manejar los resultados de la query (consulta) Insertar, Leer, Actualizar, Borrar (Create,Read,Update,Delete)
#5-Cerrar puntero
#6-Cerrar conexion

import sqlite3

miConexion = sqlite3.connect('Primera Base')
miCursor = miConexion.cursor()

#Para crear tablas
#miCursor.execute("CREATE TABLE Productos (nombre_articulo VARCHAR(50), precio INT, seccion VARCHAR(20))")
#La sentencia anterior la debemos ejecutar solo la primera vez que ejecutamos la aplicacion y despues
#debemos comentarlas

#Para agregar un valor a la tabla
miCursor.execute("INSERT INTO Productos VALUES ('Balon de futbol',15,'Deportes')")
#La sentencia anterior tambien se borra

variosProductos = [
    ("Camisa",10,"Deportes"),
    ("Jarron",10,"Ceramica"),
    ("Camion",10,"Jugueteria")
]

#Insertamos
miCursor.executemany('INSERT INTO Productos VALUES (?,?,?)',variosProductos)
miCursor.execute('SELECT * FROM Productos')
listaProductos = miCursor.fetchall()
#print(listaProductos)

for producto in listaProductos:
    print(producto)
    print(producto[0])


#Luego cerramos la conexion
miCursor.close()
print('Ejecucion terminada')