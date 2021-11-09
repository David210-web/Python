#Serializar objetos
import pickle

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f'La marca es: {self.marca} y el modelo es: {self.modelo}')

coche1 = Vehiculo('Mazda','MX5')
coche2 = Vehiculo('Toyota','Corolla')
coche3 = Vehiculo('Nissan','Sentra')

coches = [coche1,coche2,coche3]

fichero = open('losCoches','wb')
pickle.dump(coches,fichero)
fichero.close()

#Recibir los objetos
ficheroApertura = open('losCoches','rb')
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
    print(c.estado()) #Para ver su informacion