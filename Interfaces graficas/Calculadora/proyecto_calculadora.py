from tkinter import *
raiz = Tk()
raiz.title('Calculadora')
raiz.iconbitmap('imagen.ico')

miFrame = Frame(raiz)
miFrame.pack()
miFrame.config(padx=5, pady=5)


#Intefaz de Pantalla
numeroPantalla = StringVar()
pantalla = Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1, column= 1, pady=5, columnspan=4)
pantalla.config(bg="black",fg="#03f943",justify="right")

#--Funcionalidades--
#variables globales
#Variables generales
operacion = ''
resultado = 0
reset_pantalla = False
#Variables para resta

#--Al pulsar numero aparecera en pantalla--
def pulsarNumero(num):
    global operacion
    global reset_pantalla
    if reset_pantalla != False:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#--Borrar datos--
def borrar():
    numeroPantalla.set('')

#--Funciones suma--
def suma(num):
    global operacion
    global resultado
    resultado += int(num)
    operacion = 'suma'
    numeroPantalla.set(resultado)

#--Funcion resta--
num1 = 0
contador_resta = 0
def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_resta = contador_resta+1
    operacion = "resta"
    reset_pantalla = True

#--Funcion multiplica--
contador_multi = 0
def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_multi = contador_multi + 1
    operacion = 'multiplicacion'
    reset_pantalla = True

#--Funcion Division--
contador_divi = 0
def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_divi == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_divi = contador_divi + 1
    operacion = 'division'
    reset_pantalla = True

#--Funcion de resultado--
def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    if operacion == 'suma':
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0
    elif operacion == 'resta':
        numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == 'multiplicacion':
        numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == 'division':
        numeroPantalla.set(int(resultado) / int(numeroPantalla.get()))
        resultado = 0
        contador_divi = 0

#Botones
#Primera fila de botones
btn9 = Button(miFrame,text="9",width=3,command= lambda : pulsarNumero("9"))
btn9.grid(row=2,column=1,padx=2,pady=2)
btn9.config(bg="#4682b4", fg="white")

btn8 = Button(miFrame,text="8",width=3,command= lambda : pulsarNumero("8"))
btn8.grid(row=2,column=2,padx=2,pady=2)
btn8.config(bg="#4682b4", fg="white")

btn7 = Button(miFrame, text='7', width=3, command= lambda : pulsarNumero("7"))
btn7.grid(row=2,column=3,padx=2,pady=2)
btn7.config(bg="#4682b4", fg="white")

btnMult = Button(miFrame, text='X', width=3, command= lambda : multiplica(numeroPantalla.get()))
btnMult.grid(row=2,column=4,padx=2,pady=2)
btnMult.config(bg="#b22222", fg="white")

#Segunda fila de datos
btn4 = Button(miFrame,text="4",width=3,command= lambda : pulsarNumero("4"))
btn4.grid(row=3,column=1,padx=2,pady=2)
btn4.config(bg="#4682b4", fg="white")

btn5 = Button(miFrame,text="5",width=3,command= lambda : pulsarNumero("5"))
btn5.grid(row=3,column=2,padx=2,pady=2)
btn5.config(bg="#4682b4", fg="white")

btn6 = Button(miFrame, text='6', width=3, command= lambda : pulsarNumero("6"))
btn6.grid(row=3,column=3,padx=2,pady=2)
btn6.config(bg="#4682b4", fg="white")

btnDiv = Button(miFrame, text='/', width=3, command= lambda : divide(numeroPantalla.get()))
btnDiv.grid(row=3,column=4,padx=2,pady=2)
btnDiv.config(bg="#b22222", fg="white")

#Tercera fila de datos
btn3 = Button(miFrame,text="3",width=3,command= lambda : pulsarNumero("3"))
btn3.grid(row=4,column=1,padx=2,pady=2)
btn3.config(bg="#4682b4", fg="white")

btn2 = Button(miFrame,text="2",width=3,command= lambda : pulsarNumero("2"))
btn2.grid(row=4,column=2,padx=2,pady=2)
btn2.config(bg="#4682b4", fg="white")

btn1 = Button(miFrame, text='1', width=3, command= lambda : pulsarNumero("1"))
btn1.grid(row=4,column=3,padx=2,pady=2)
btn1.config(bg="#4682b4", fg="white")

btnRes = Button(miFrame, text='-', width=3, command= lambda : resta(numeroPantalla.get()))
btnRes.grid(row=4,column=4,padx=2,pady=2)
btnRes.config(bg="#b22222", fg="white")

#Cuarta fila de datos
btn0 = Button(miFrame,text="0",width=3,command= lambda : pulsarNumero("0"))
btn0.grid(row=5,column=1,padx=2,pady=2)
btn0.config(bg="#4682b4", fg="white")

btnComa = Button(miFrame,text=",",width=3,command= lambda : pulsarNumero(","))
btnComa.grid(row=5,column=2,padx=2,pady=2)
btnComa.config(bg="#4682b4", fg="white")

btnSuma = Button(miFrame, text='+', width=3, command= lambda : suma(numeroPantalla.get()))
btnSuma.grid(row=5,column=3,padx=2,pady=2)
btnSuma.config(bg="#b22222", fg="white")

btnIgual = Button(miFrame, text='=', width=3, command = lambda : el_resultado())
btnIgual.grid(row=5,column=4,padx=2,pady=2)
btnIgual.config(bg="#b22222", fg="white")

#Boton borrar
botonDelete = Button(miFrame,text="Delete",width=8,command=lambda : borrar())
botonDelete.grid(row=6,column=0,columnspan=4,pady=3)
botonDelete.config(bg="#b22222",fg="white")

#Creamos la ventana
raiz.mainloop()