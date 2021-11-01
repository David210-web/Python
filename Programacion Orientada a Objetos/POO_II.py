#Constructor, Estado inicial y encapuslacion
class Coche():
    #Propiedades de la clase
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    color = "azul"

    #Metodos de la clase (Una funcion especial que pertenece a la clase)
    def arrancar(self): #El parametro por defecto es self (es como el this en Java o Javascript)
        self.enmarcha = True #Para acceder a una propiedad y modificarla dentro de una clase
        #pass #El pass es para que si no queremos ejecutar nada no nos de un fallo

    def estado(self):
        if self.enmarcha:
            return 'El coche esta en marcha'
        else:
            return 'El coche está parado'

miCoche = Coche()
print(f"{miCoche.largoChasis}--{miCoche.anchoChasis}--{miCoche.ruedas}--{miCoche.enmarcha}--{miCoche.color}")
print(miCoche.estado())
