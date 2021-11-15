#Aprenderemos a como usar los labels
from tkinter import *

raiz = Tk()
raiz.title('Uso del label')
miFrame = Frame(raiz,width="720",height="360")
miFrame.pack()

#Ahora pondremos el label
miLabel = Label(miFrame,text="Este es un label de la interfaz de python")
miLabel.pack()
miLabel.place(x="250",y="130")
raiz.mainloop()