#Crear inputs para textos largos,scrooll y botones
from tkinter import *
#Configuracion Basica
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()
raiz.title('Agregar botones')
raiz.iconbitmap('imagen.ico')

#Crear Label
comentariosLabel = Label(miFrame,text="Dinos lo que piensa:")

#Crear objetos
comentariosTexto = Text(miFrame,width=20,height=5)
scroollBar = Scrollbar(miFrame,command=comentariosTexto.yview)
scroollBar.grid(row=0,column=2,sticky="nse") #El "nse" es para ajustar la altura del scrooll al widget
comentariosTexto.config(yscrollcommand=scroollBar.set) #Para incorporar el scroll adentro del widget

#Accion del boton
miNombre = StringVar()
labelNombre = Label(miFrame,text="Ingrese tu nombre")
labelNombre.grid(row=1,column=0,padx=10,pady=10)
inputNombre = Entry(miFrame,textvariable = miNombre)
inputNombre.grid(row=1,column=1,padx=10,pady=10)


def accionBtn():
    miNombre.set('David')


#Agregar botones
btnAccion = Button(raiz,text="Mostrar",command=accionBtn) #El text es para el valor del boton y el command para la
#accion que hara

btnAccion.pack()


#Agregar acciones

#Ordenar los objetos
comentariosLabel.grid(row=0,column=0,padx=10,pady=10,sticky="w")
comentariosTexto.grid(row=0,column=1,padx=10,pady=10,sticky="w")

raiz.mainloop()

#Datos a saber:
#Button(command=accion) para crear un boton y este parametro es la accion que hara
#Scrollbar(command=comentariosTexto.yview) para crear una barra de scrooll y el parametro es que sera un escrooll en eje vertical
#La propiedad sticky="nse") en la funcion .grid() es para ajustar la altura del scrooll al widget
#StringVar() para crear una variable de tipo string pero esta estara vacia
#.set() para agregar el dato a la variable hecha con StringVar() que esta vacia