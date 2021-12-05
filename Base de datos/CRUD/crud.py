from tkinter import *
from tkinter import messagebox
import sqlite3

#--Funciones--
#--Conexion a base de dtos (Pestaña BBDD)--
def conexionBBDD():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''CREATE TABLE DATOSUSUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_USUARIO VARCHAR(50), PASSWORD VARCHAR(50), APELLIDO VARCHAR(10), DIRECCION VARCHAR(50),COMENTARIOS VARCHAR(100))''')
        messagebox.showinfo("BBDD","Base de datos creada con exito")
    except:
        messagebox.showwarning("¡ATENCION!","La base de datos ya existe")


def salirAplicacion():
    valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
    if valor == "yes":
        raiz.destroy()


#--Borrar campos (Pestaña Borrar)--
def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoComentario.delete(1.0,END) #Punto de partida para comenzar y el otro es el punto final


#---------Insertar campos en Base de datos (Pestaña CRUD y boton CREATE)---------
def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos = miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END)
    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+ miNombre.get() +
                     "','" + miPass.get() +
                     "','" + miApellido.get() +
                     "','" + miDireccion.get() +
                     "','" + textoComentario.get("1.0", END) + "')")"""
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro Realizado con exito")

#---------Leer campos de la base de datos (Pestaña crud y boton Read)---------
def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = " + miId.get())
    elUsuario = miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert(1.0,usuario[5])

    miConexion.commit()

#---------Actualizar registros de la base de datos (Pestaña crud y boton UPDATE)---------
def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    datos = miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END)
    """miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
                     "', PASSWORD= '" + miPass.get() +
                     "', APELLIDO= '" + miApellido.get() +
                     "', DIRECCION= '" + miDireccion.get() +
                     "', COMENTARIOS= '" + textoComentario.get("1.0",END) +
                     "'WHERE ID =" + miId.get())"""
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?,APELLIDO= ?, DIRECCION= ?,COMENTARIOS= ?"+
                     "WHERE ID =" + miId.get(),(datos))
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro Actualizado con exito")

#---------Eliminar registros de la base de datos (Pestaña crud y boton DELETE)---------
def eliminar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID =" + miId.get())
    miConexion.commit()

    messagebox.showinfo("BBDD","Registro borrado con exito")

#--Interfaz grafica--
raiz = Tk()
raiz.title("Crud de Python")

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu,width=300,height=300)

#---------Pestaña menu---------
db = Menu(barraMenu,tearoff=0)
db.add_command(label="Conectar",command=conexionBBDD)
db.add_command(label="Salir",command=salirAplicacion)

#---------Pestaña Borrar---------
borrardb = Menu(barraMenu,tearoff=0)
borrardb.add_command(label="Borrar Campos",command=limpiarCampos)

#---------Pestaña CRUD---------
crudMenu = Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

#---------Pestaña ayuda---------
ayudaMenu = Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="licensia")
ayudaMenu.add_command(label="Acerca de")

#---------Agregar el menu a la aplicacion---------
barraMenu.add_cascade(label="BBDD",menu=db)
barraMenu.add_cascade(label="Borrar",menu=borrardb)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

#----Frame y widgets de la primera zona (Comienzo de campos)----
miFrame = Frame(raiz)
miFrame.pack()

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDireccion = StringVar()

#Inputs de entrada
#--ID--
cuadroID = Entry(miFrame,textvariable=miId)
cuadroID.grid(row=0,column=1,padx=10,pady=10)

#--Nombre--
cuadroNombre = Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

#--Password--
cuadroPassword = Entry(miFrame,textvariable=miPass)
cuadroPassword.grid(row=2,column=1,padx=10,pady=10)
cuadroPassword.config(show="*")

#--Apellido--
cuadroApellido = Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

#--Direccion--
cuadroDireccion = Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

#--Comentario--
textoComentario = Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5,column=1,sticky="nse")

textoComentario.config(yscrollcommand=scrollVert.set)

#--Label--
idLabel = Label(miFrame,text="ID:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel = Label(miFrame,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel = Label(miFrame,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel = Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel = Label(miFrame,text="Direccion:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentarioLabel = Label(miFrame,text="Comentarios:")
comentarioLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#--Botones--
miFrame2 = Frame(raiz)
miFrame2.pack()

botonCrear = Button(miFrame2,text="Create",command=crear)
botonCrear.grid(row=1,column=0,padx=5,pady=5)

botonLeer = Button(miFrame2,text="Read",command=leer)
botonLeer.grid(row=1,column=1,padx=5,pady=5)

botonActualizar = Button(miFrame2,text="Update",command=actualizar)
botonActualizar.grid(row=1,column=2,padx=5,pady=5)

botonBorrar = Button(miFrame2,text="Delete",command=eliminar)
botonBorrar.grid(row=1,column=3,padx=5,pady=5)

raiz.mainloop()