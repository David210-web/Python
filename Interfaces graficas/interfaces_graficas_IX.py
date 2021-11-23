#--Botones de radio--
from tkinter import *
raiz = Tk()
raiz.title('Botones de radio')
raiz.config(width=300,height=300)

frame = Frame(raiz)
frame.pack()

def imprimir():
    print(varOpcion.get())
    if varOpcion.get() == 1:
        print('Maculino')
        etiqueta.config(text="El genero es Masculino")
    else:
        print('Femenino')
        etiqueta.config(text="El genero es Femenino")




varOpcion = IntVar()
Label(frame,text="Genero:").pack()
Radiobutton(frame,text="Masculino",variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(frame,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()

etiqueta = Label(frame)
etiqueta.pack()

raiz.mainloop()