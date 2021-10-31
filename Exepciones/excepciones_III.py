#Instruccion Raise (para provocar una excepcion no que el programa lo haga)
#Uso del Raise
def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edaddes negativas")

    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate..."

print(evaluaEdad(-15))


import math #Importamos la clase math
def calculaRaiz(num1):
	if num1 < 0:
		raise ValueError('El numero no puede ser negativo')
	else:
		return math.sqrt(num1)

try:
	op1 = (int(input('Introduce un numero: '))
except ValueError as ErrorNumNegativo: #(Tiene que ser el mismo tipo de error que esta en el raise)
	print('ErrorNumNegativo')

print(calculaRaiz(op1))

print("Programa terminado")