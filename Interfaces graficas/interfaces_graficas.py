#Crear inputs
from tkinter import *

#Cuadro basico
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

#Creacion de input
inputNombre = Entry(miFrame)
inputApellido = Entry(miFrame)
inputPassword = Entry(miFrame)
#inputNombre.pack()

#Creando los label para identificar
miLabel = Label(miFrame,text="Ingrese nombre:")
apellidoLabel = Label(miFrame,text="Ingrese tu apellido:") #La opcion pack() no se usa en estos casos
passwordLabel = Label(miFrame,text="Ingrese tu password: ")
#miLabel.pack()

#Ordenamos los widgets
miLabel.grid(row=0,column=0,padx=10,pady=10,sticky="w")
inputNombre.grid(row=0,column=1,padx=10,pady=10)

apellidoLabel.grid(row=1,column=0,padx=10,pady=10,sticky="w")
inputApellido.grid(row=1,column=1,padx=10,pady=10)

passwordLabel.grid(row=2,column=0,padx=10,pady=10,sticky="w")
inputPassword.grid(row=2,column=1,padx=10,pady=10,sticky="w")

#Configurar detalles
#Para configurar un password podemos hacer esto:
inputPassword.config(show="*")
inputNombre.config(justify="center")

#Creamos la ventana
raiz.mainloop()

#Datos a recordad:
#Entry() Para crear inputs
#grid(row,column,sticky) para alinear con grid los objetos por eso el row(fila) y column(columna) o sticky(alinear)
#padx,pady Para poner padding en X o en Y
#.config(show="*") Para ocultar lo que escribimos en el input
#.config(justify="center") Para alinear como Text-align en CSS