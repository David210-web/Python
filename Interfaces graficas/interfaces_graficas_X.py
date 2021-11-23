#--Checkbutton--
from tkinter import *
raiz = Tk()
raiz.title('Checkbutton')

miFrame = Frame(raiz)
miFrame.pack()

playa = IntVar()
Montaña = IntVar()
Campos = IntVar()

def opcionesViajes():
    opcionEscogida = ''
    if playa.get() == 1:
        opcionEscogida += 'playa'

    if Montaña.get() == 1:
        opcionEscogida += 'Montaña'

    if Campos.get() == 1:
        opcionEscogida += 'Campos'

    textoFinal.config(text=opcionEscogida)

opcion = Label(miFrame,text="Elige opciones")
opcion.pack()

Checkbutton(miFrame,text="Montaña",variable=playa,onvalue=1,offvalue=0,command=opcionesViajes).pack()
Checkbutton(miFrame,text="Playa",variable=Montaña,onvalue=1,offvalue=0,command=opcionesViajes).pack()
Checkbutton(miFrame,text="Campos",variable=Campos,onvalue=1,offvalue=0,command=opcionesViajes).pack()

textoFinal = Label(raiz)
textoFinal.pack()

raiz.mainloop()