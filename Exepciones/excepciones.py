#Excepciones en python
#Las excepciones son errores que ocurren durante la ejecucion del programa
#La sintaxis del codigo es correcta pero durante la ejecucion ha ocurriod "Algo inesperado"
#Cuando todo esta bien
# en el codigo pero aun asi hay un error en el programa y si eso pasa el programa se cae
#porque se hay un error en una linea las otras instrucciones no se cargan


def suma(num1,num2):
    return num1 + num2


def resta(num1,num2):
    return num1 - num2

def multiplica(num1,num2):
    return num1 * num2

def divide(num1,num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('No se puede dividir por 0')
        return 'Operacion erronea'

dato1 = int(input('Ingrese el primer dato'))
dato2 = int(input('Ingrese el segundo dato'))

operacion = input('Introduce la operacion a realizar: suma,resta,multiplica,divide')

if operacion == 'suma':
    print(suma(dato1,dato2))
elif operacion == 'resta':
    print(resta(dato1,dato2))
elif operacion == 'multiplica':
    print(multiplica(dato1,dato2))
elif operacion == 'divide':
    print(divide(dato1,dato2))
else:
    print('Operacion no encontrada')

print('Operacion ejecutada, Continuacion de ejecucion del programa')

#Para poder controlar estos erroes hacemos algo que se llama manejo de control de excepciones
#y esta consiste en que al menos intente ejecutar la linea de codigo y si no se puede ejecutar
#que al menos permita ejecutar el resto de codigo que antes no se podia ejecutar por el error


#para controlar las exepciones es (ver en la funcion divide)
