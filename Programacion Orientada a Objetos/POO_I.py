#Creando las clases de los objetos
#Creando las clases de los objetos
class Coche():
    #un constructor es un metodo especial que le da un
    #estado inical a un objeto
    #para hacer un constructor es asi:

    def __init__(self): #Este es el constructor de esta clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #2 guiones bajos para encapsular
        #La variable no podra ser accedida afuera de la clase
        #pero si podra ser accedida adentro de la clase
        self.__enmarcha = False

    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'

    def estado(self):
        print(
            f"El coche tiene {self.__ruedas}. "
            f"un ancho de {self.__anchoChasis}. "
            f"un largo de {self.__largoChasis}."
        )

miCoche = Coche()
#Con esto podemos modificar esta propiedad pero esto no deberia permitirse
miCoche.ruedas = 2
print(miCoche.arrancar(True))
miCoche.estado()

#Para encapsular o proteger una clase para que no se pueda modificar
#osea encapsular pues se hace con dos guiones bajos a la variable
#Y podemos encapsular metodos