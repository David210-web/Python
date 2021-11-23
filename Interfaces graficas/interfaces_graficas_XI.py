#--Menu--
from tkinter import *
root = Tk()
root.title('Menu Personalizado')
root.geometry('760x320')

miFrame = Frame(root)
miFrame.pack()

opcion = IntVar()
def funcion():
    if opcion.get() == 1:
        labelOpcion.config(text="Has elegido la seleccion 1")
    else:
        labelOpcion.config(text="Has elegido la seleccion 2")

#Creando el menu general
navBar = Menu(root)
root.config(menu=navBar) #En la raiz ira el navbar en la opcion menu

#Creamos la opciones principales que tendra el menu (Archivo,Edicion ...)
menuArchivo = Menu(navBar,tearoff=0) #Estas iran ancladas al Objeto Menu
menuEdicion = Menu(navBar,tearoff=0)
menuHerramientas = Menu(navBar,tearoff=0)
menuAyuda = Menu(navBar,tearoff=0)

#Pero para que se muestre en pantalla tenemos que mostrar los textos de las variables (Archivo,edicion...)
#Para agregarle el label es con la propiedad .add_cascade con la propiedad label y anclado a la propiedad menu
navBar.add_cascade(label="Archivo",menu=menuArchivo)
navBar.add_cascade(label="Edicion",menu=menuEdicion)
navBar.add_cascade(label="Herramientas",menu=menuHerramientas)
navBar.add_cascade(label="Ayuda",menu=menuAyuda)

#Para poner las opciones de los menus es:
#de la opcion archivo
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Cerrar")
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir")

#de la opcion edicion
menuEdicion.add_command(label="Cortar")
menuEdicion.add_command(label="Copiar")
menuEdicion.add_command(label="Pegar")
menuEdicion.add_separator()
menuEdicion.add_command(label="Seleccionar todo")

#de la opcion Herramientas
menuHerramientas.add_command(label="Paleta de comandos")
menuHerramientas.add_command(label="Snippets")
menuHerramientas.add_command(label="Construir Sistema")
menuHerramientas.add_separator()
menuHerramientas.add_command(label="Salir")

#de la opcion Ayuda
menuAyuda.add_command(label="Documentacion")
menuAyuda.add_command(label="Redes Sociales")

miLabel = Label(miFrame,text="Menu Personalizado")
miLabel.pack()

btn = Button(miFrame,text="Enviar")
btn.pack()

Radiobutton(miFrame,text="Seleccion 1",variable=opcion,value=1,command=funcion).pack()
Radiobutton(miFrame,text="Seleccion 2",variable=opcion,value=2,command=funcion).pack()

labelOpcion = Label(miFrame)
labelOpcion.pack()

root.mainloop()