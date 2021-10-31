#Generadores Parte I
#1-Son estructuras que extraen valores de una funcion y se almacenan en objetos iterables
#(que se pueden recorrer)
#2-Estos valores se almacenan de uno en uno
#3-Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que
#se solicita. Esta caracteristica es conocida como "Suspension de estado"

#Generadores ¿Que utilidad tienen?
#- Son mas eficientes que las funciones tradicionales
#- Muy utiles con lista de valores infinitos
#- Bajo determinados escenarios, será muy util que un generador devuelva los valores de uno en uno

#En los generadores usamos la palabra clave yield
#Ejemplo practico

#Funcion normal
def generarPares(limites):
    num = 1
    listaPares = []
    while num < limites:
        listaPares.append(num * 2)
        num += 1
    return listaPares

print(generarPares(10))

#para generadores
def generarPares2(limite):
    num = 1
    #aqui la lista de los pares ya no esta porque ya el generador nos devuelve una lista
    while num < limite:
        yield num * 2 #Aqui hacemos dos cosas: el append() y el returno el yield hace ya todo el trabajo
        num += 1

devuelvePares = generarPares2(10) #creamos la variable para poder iterar el objeto

#for i in devuelvePares:
#    print(i) #ja chupenla

print(next(devuelvePares))
print("---Aqui puede ir mas codigo---")

print(next(devuelvePares))
print("---Aqui puede ir mas codigo---")

print(next(devuelvePares))
print("---Aqui puede ir mas codigo---")

#lo puedes hacer tambien con la funciones pero los generadores en este caso son mejores porque
#para acceder a los tres primeros en la lista con las funciones tenemos que crear TODA la lista no solo lo primero
#tres datos y esto baja en rendimiento y gasta mas espacion en memoria en cambio con llamar al generador con next
#solo genera un dato, no genera toda la lista completa, cada vez que que llames se generara un numero de la lista
#hasta llegar a su limite