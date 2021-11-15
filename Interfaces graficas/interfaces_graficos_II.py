#Interfaces graficas II
from tkinter import *

raiz = Tk()
raiz.title("Ventana de prueba")
raiz.config(bg="blue")
miFrame = Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="650",height="350")
raiz.config(relief="groove")
raiz.config(bd="2")
miFrame.config(cursor="hand2")
raiz.mainloop()