#--Ventanas Emergentes--
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Ventana Modal')
root.geometry('1080x720')
miFrame = Frame(root)
miFrame.pack()

navBar = Menu(root)
root.config(menu=navBar)

def ventanaInformacion():
    messagebox.showinfo('Ventana de informacion','Este es un mensaje de una ventana de informacion')

def ventanaAlerta():
    messagebox.showwarning('Licencia','Producto bajo licencia')

def ventanaSeleccion():
    valor = messagebox.askquestion('Salir','¿Desea salir de la App?')
    if valor == 'yes':
        root.destroy()
        print('Proceso terminado')

def ventanaSeleccionBoolean():
    valor = messagebox.askokcancel('Cerrar','¿Deseas cerrar el documento?')
    if valor:
        root.destroy()


def ventanaEmergencia():
    valor = messagebox.askretrycancel('Reintentar','No es posible cerrar Documento')
    if valor:
        messagebox.showinfo('Reintentando','Archivo reintentando conectar')
        miLabel = Label(miFrame,text="Todo esta correcto")
        miLabel.pack()
    else:
        root.destroy()
        print('Operacion terminada')


menuArchivo = Menu(navBar,tearoff=0)
menuEditar = Menu(navBar,tearoff=0)
menuHelp = Menu(navBar,tearoff=0)

navBar.add_cascade(label="Archivo",menu=menuArchivo)
navBar.add_cascade(label="Editar",menu=menuEditar)
navBar.add_cascade(label="Ayuda",menu=menuHelp)

menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Cerrar",command=ventanaSeleccionBoolean)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir",command=ventanaSeleccion)

menuEditar.add_command(label="Seleccionar")
menuEditar.add_command(label="Copiar")
menuEditar.add_command(label="Cortar")
menuEditar.add_command(label="Pegar")

menuHelp.add_command(label="Licencia",command=ventanaAlerta)
menuHelp.add_command(label="Sobre mi",command=ventanaInformacion)
menuHelp.add_command(label="Cancelar",command=ventanaEmergencia)



root.mainloop()