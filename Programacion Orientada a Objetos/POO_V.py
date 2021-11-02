#Herencia:
#Sobre escritura de metodos
#Herencia simple y multiple

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

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado = cargar
        if self.cargado:
            return 'La furngoneta está cargada'
        else:
            return 'No esta cargada'

class Moto(Vehiculos): #Construiremos la clase moto
    hcaballito = "No hace el caballito"
    def caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'

    #Vamos a sobreescribir el metodo estado
    def estado(self):
        print(
            f"Marca: {self.marca} \n"
            f"Modelo: {self.modelo}\n"
            f"{self.hcaballito}"
        )

miMoto = Moto('Susuki','ninja')
miMoto.caballito()
print(miMoto.hcaballito)
miMoto.estado()


miFurgoneta = Furgoneta('Renault','Kangoo')
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#Imaginemonos que queremos dar soporte a vehiculos electricos

class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

#Herencia multiple
class BicicletaElectrica(VElectricos,Vehiculos):
    pass

#Cuando hay herencia multiple se da preferencia a la primera clase que pusiste
#en los parentesis, entonces aqui heredamos el constructor de VElectricos
miBici = BicicletaElectrica()