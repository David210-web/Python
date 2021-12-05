from tkinter import *
from tkinter import messagebox
import mysql.connector

#Ajustes basicos de la interfacas con su frame principal
root = Tk()
root.title("Agregar y Ver registros")
miFrame = Frame(root)
miFrame.pack()
miFrame.config(padx=5,pady=5)

#Conexion a base de datos
conexion = mysql.connector.connect(
        host = 'localhost',
		port = 3306,
		user = 'root',
		db = 'ejemplo'
)

cursor = conexion.cursor()

if conexion.is_connected():
    print("Conexion Exitossa")



#Frame para los botones
frameBotones = Frame(miFrame)
frameBotones.pack()

#Variables globales
nombreData = StringVar()
categoriaData = StringVar()

#Funcion Para ingresar datos
def ingresar():
    global nombreData
    global categoriaData

    datoNuevo = Frame(miFrame)
    datoNuevo.pack()

    nombre = Entry(datoNuevo,textvariable=nombreData)
    categoria = Entry(datoNuevo,textvariable=categoriaData)

    nombreLabel = Label(datoNuevo,text="Nombre")
    categoriaLabel = Label(datoNuevo,text="Categoria")

    nombreLabel.grid(row=2,column=1)
    nombre.grid(row=3,column=1,columnspan=4,pady=2)

    categoriaLabel.grid(row=4,column=1)
    categoria.grid(row=5,column=1,columnspan=4,pady=2)

    def enviar(): #Funcion para confirmar el registro de datos
        print("Dato enviado")
        print(f"Datos: {nombreData.get()} y {categoriaData.get()}")
        messagebox.showinfo('Registro Completado', 'El registro ha sido añadido con exito')
        datoNuevo.pack_forget()

    confimar = Button(datoNuevo,text="Enviar datos",command=enviar)
    confimar.grid(row=6,column=1,columnspan=4, pady=2)


#Funcion Para mostrar Datos
def mostrar():
    infoFrame = Frame(miFrame)
    infoFrame.pack()
    infoFrame.config(pady=3)
    cursor.execute("SELECT * FROM ejemplo")
    datos = cursor.fetchall()
    for dato in datos:
        #-----Etiqueta-----
        idLabel = Label(infoFrame,text="ID")
        idLabel.grid(row=2, column=1)
        #-------Dato-----
        idInfo = Label(infoFrame, text=dato[0])
        idInfo.grid(row=3, column=1)

        #-----Etiqueta-----
        nombreLabel = Label(infoFrame,text="Nombre")
        nombreLabel.grid(row=2, column=2)
        #-----Dato-----
        nombreInfo = Label(infoFrame, text=dato[1])
        nombreInfo.grid(row=3, column=2)

        #-----Etiqueta-----
        categoriaLabel = Label(infoFrame, text="Nombre")
        categoriaLabel.grid(row=2, column=3)
        #-----Dato-----
        categoriaInfo = Label(infoFrame, text=dato[2])
        categoriaInfo.grid(row=3, column=3)
        #print(dato)

#Botones
btnAgregar = Button(frameBotones,text="Agregar Datos",command=ingresar)
btnAgregar.grid(row=1,column=1,padx=3,pady=3)
btnAgregar.config(pady=3,padx=3,bg="steel blue",fg="#fff")

btnMostrar = Button(frameBotones,text="Mostrar Datos",command=mostrar)
btnMostrar.grid(row=1,column=3,padx=3,pady=3)
btnMostrar.config(pady=3,padx=3,bg="red2",fg="#fff")

#Correr la interfaz
conexion.close()
root.mainloop()