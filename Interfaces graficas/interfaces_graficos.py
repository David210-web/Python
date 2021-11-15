#-- INTERFACES GRAFICAS I --
from tkinter import * #Importamos las librerias

raiz = Tk()
raiz.title("Ventana de prueba") #Creamos el titulo de la ventana
raiz.resizable(False,False) #Para redimensionar las ventanas (Width,Height) Son los parametros
raiz.iconbitmap("imagen.ico")
raiz.geometry("1080x766")
raiz.mainloop() #Creamos la ventana