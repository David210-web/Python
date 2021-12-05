import mysql.connector
from tkinter import *

raiz = Tk()
raiz.title('Prueba')
miFrame = Frame(raiz)
raiz.geometry('720x360')
miFrame.pack()


conexion = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password= '',
    db="ejemplo"
)

if conexion.is_connected():
    print('Conexion exitosa')
    miCursor = conexion.cursor()
    #miCursor.execute(f'INSERT INTO ejemplo (nombre,precio,seccion) VALUES("Bola",8,"Ejercicio")')
    #miCursor.execute("UPDATE ejemplo SET seccion='Ropa' WHERE nombre = 'Camisa'")
    miCursor.execute("DELETE FROM ejemplo")
    print('Dato eliminado')
    miCursor.execute('SELECT * FROM ejemplo')
    datos = miCursor.fetchall()
    def mostrar():
        for dato in datos:
            lienzo = Label(miFrame,text=f"{dato[0]} - {dato[1]} - {dato[2]}")
            lienzo.pack()
    btn = Button(miFrame,text='Mostrar Datos',command=mostrar)
    btn.pack()

conexion.commit()
conexion.close()
raiz.mainloop()