#Herencia
#Clase padre
class Vehiculos():
    def __init__(self, marca , modelo):
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
        print(
            f"Marca: {self.marca} \n"
            f"Modelo: {self.modelo}"
        )

#Motocicleta con herencia de vehiculo
class Moto(Vehiculos): #Se pone en los parentesis la clase que queremos heredar
    pass

miMoto = Moto('Susuki','ninja')
miMoto.estado()