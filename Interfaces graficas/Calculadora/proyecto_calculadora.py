#Calculadora

#Configuracion Basica
from tkinter import *
raiz = Tk()
raiz.title('Calculadora')
raiz.iconbitmap('imagen.ico')
miFrame = Frame(raiz)

miFrame.pack()
miFrame.config(padx=5,pady=5)

#Funciones




#Creamos la pantalla (Sera un input)

numeroPantalla = StringVar()
pantalla = Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,pady=5,columnspan=4)
pantalla.config(bg='black',fg="#03f943", justify="right")

#--Funcionalidades--
operacion = ''
resultado = 0

def pulsarNumero(num):
    global operacion
    if operacion != "":
        numeroPantalla.set(num)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#--Suma--
def suma(num):
    global operacion
    global resultado
    resultado += int(num)
    operacion = 'suma'
    numeroPantalla.set(resultado)


#--Resultado--
def el_resultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0

#--Primera fila de datos--
btn9 = Button(miFrame,text='9',width=3,command=lambda : pulsarNumero("9"))
btn9.grid(row=2,column=1,padx=2,pady=2)
btn9.config(bg="#4682B4",fg="white")

btn8 = Button(miFrame,text='8',width=3,command=lambda : pulsarNumero("8"))
btn8.grid(row=2,column=2,padx=2,pady=2)
btn8.config(bg="#4682B4",fg="white")


btn7 = Button(miFrame,text='7',width=3,command=lambda : pulsarNumero("7"))
btn7.grid(row=2,column=3,padx=2,pady=2)
btn7.config(bg="#4682B4",fg="white")

btnMult = Button(miFrame,text='X',width=3)
btnMult.grid(row=2,column=4,padx=2,pady=2)
btnMult.config(bg="#B22222",fg="white")


#--Segunda fila de datos
btn4 = Button(miFrame,text='4',width=3,command=lambda : pulsarNumero("4"))
btn4.grid(row=3,column=3,padx=2,pady=2)
btn4.config(bg="#4682B4",fg="white")


btn5 = Button(miFrame,text='5',width=3,command=lambda : pulsarNumero("5"))
btn5.grid(row=3,column=2,padx=2,pady=2)
btn5.config(bg="#4682B4",fg="white")


btn6 = Button(miFrame,text='6',width=3,command=lambda : pulsarNumero("6"))
btn6.grid(row=3,column=1,padx=2,pady=2)
btn6.config(bg="#4682B4",fg="white")


btnDiv = Button(miFrame,text='/',width=3)
btnDiv.grid(row=3,column=4,padx=2,pady=2)
btnDiv.config(bg="#B22222",fg="white")


#--Tercera fila de datos--
btn3 = Button(miFrame,text='3',width=3,command=lambda : pulsarNumero("3"))
btn3.grid(row=4,column=1,padx=2,pady=2)
btn3.config(bg="#4682B4",fg="white")


btn2 = Button(miFrame,text='2',width=3,command=lambda : pulsarNumero("2"))
btn2.grid(row=4,column=2,padx=2,pady=2)
btn2.config(bg="#4682B4",fg="white")


btn1 = Button(miFrame,text='1',width=3,command=lambda : pulsarNumero("1"))
btn1.grid(row=4,column=3,padx=2,pady=2)
btn1.config(bg="#4682B4",fg="white")

btnRes = Button(miFrame,text='-',width=3)
btnRes.grid(row=4,column=4,padx=2,pady=2)
btnRes.config(bg="#B22222",fg="white")

#--Cuarta fila de datos--
btn0 = Button(miFrame,text='0',width=3,command=lambda : pulsarNumero("0"))
btn0.grid(row=5,column=1,padx=2,pady=2)
btn0.config(bg="#4682B4",fg="white")


btnComa = Button(miFrame,text=',',width=3,command=lambda : pulsarNumero(","))
btnComa.grid(row=5,column=2,padx=2,pady=2)
btnComa.config(bg="#4682B4",fg="white")


btnSuma = Button(miFrame,text='+',width=3,command=lambda : suma(numeroPantalla.get()))
btnSuma.grid(row=5,column=3,padx=2,pady=2)
btnSuma.config(bg="#B22222",fg="white")


btnIgual = Button(miFrame,text='=',width=3,command=lambda : el_resultado())
btnIgual.grid(row=5,column=4,padx=2,pady=2)
btnIgual.config(bg="#B22222",fg="white")



#Creamos la ventana
raiz.mainloop()