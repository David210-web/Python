#Polimorfismo
class Coche():
    def desplazamiento(self):
        print('Me desplazo usando 4 ruedas')

class Moto():
    def desplazamiento(self):
        print('Me desplazo usando 2 ruedas')

class Camion():
    def desplazamiento(self):
        print('Me desplazo usando 6 ruedas')

miVehiculo = Moto()
miVehiculo.desplazamiento()

#Si quisieramos hacer lo mismo con un coche tendriamos que hacer lo mismo crear
#otro objeto (mismo metodo pero de clases diferentes)

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

#Pero y si tenemos un juego y aparecen monton de coches,motos,bicis, un monton de vehiculos
#y cada un con un modo de desplazamiento diferente, si quisieramos utilizar en ese juego
#tendria que ser de esa forma, pero hay otra opcion la opcion polimorfismo asi:

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento() #No sabemos a que vehiculo hace referencia no lo sabemos
    #pero podemos usar un objeto como parametro para la funcion


miCamion = Camion()
miCoche = Coche()
desplazamientoVehiculo(miCamion) #aqui esta ocurriendo el polimorfismo
#al crear el objeto y ponerlo de parametro en la funcion esta ejecutara
#el metodo que esta en el parametro dado

desplazamientoVehiculo(miCoche)