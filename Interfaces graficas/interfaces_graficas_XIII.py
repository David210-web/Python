#--Ventana emergentes para abrir archivos
from tkinter import *
from tkinter import filedialog
from io import open

root = Tk()
root.title('Seleccionar Archivos')
miFrame = Frame(root)
miFrame.pack()
root.geometry('1080x760')

def selArc():
    fichero = filedialog.askopenfilename(title="Abrir",initialdir='C:',filetypes=(('Ficheros de excel','*.xlsx'), ('Documentos de texto','*.txt'),('Todos los archivos','*.*')))
    archivo = open(fichero,'r')
    texto = archivo.read()
    print(texto)

Button(miFrame,text='Seleccionar Archivos',command=selArc).pack()

root.mainloop()