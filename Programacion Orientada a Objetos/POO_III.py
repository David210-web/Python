#Encapsulamiento de metodos
#Un metodo encapsulado puede tener ciertas utilidades como por ejemplo
#en un carro antes de encender el motor hace un chequeo general de este, y eso se comprueba
#en las luces de la salpicadera, entonces nosotro podemos crear un metodo para verificar que todo
#esta en orden


class Coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        if self.__enmarcha:
            chequeo = self.__chequeo_interno()

        if self.__enmarcha and chequeo:
            return 'El coche esta en marcha'
        elif self.__enmarcha and chequeo == False:
            return 'Algo ha salido mal con el chequo. No podemos arrancar'
        else:
            return 'El coche esta parado'

    def estado(self):
        print(
            f"El coche tiene {self.__ruedas}. "
            f"un ancho de {self.__anchoChasis}. "
            f"un largo de {self.__largoChasis}."
        )

    #Nosotros no queremos que el metodo de chequeo sea accesible porque esa funcion la hace
    #internamente el objeto (En este caso el carro), porque si no podremos acceder en cualquier
    #momento al metodo aunque el auto este apagado y eso no tiene logica porque esta parado
    #Entonces para evitar este comportamiente tenemos que encapsular el metodo para que solo
    #se pueda usar dentro de la clase y esto se hace igual que las variable con dos guiones bajos

    def __chequeo_interno(self):
        print('-Realizando chequo interno-')
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'
        if self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas':
            return True
        else:
            return False

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

#Entonces desde fuera no saldra la opcion de chequeo interno