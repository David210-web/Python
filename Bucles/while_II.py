#Como hacer que el bocle while no sea infinito
import math

print('----Programa de calculo de raiz cuadrada----')
numero = int(input('Introduce un numero, por favor: '))
intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")
    if intentos == 2:
        print('Has echo demasiados intentos, programa terminado')
        break #Sale del bucle
    numero = int(input('Introduce un numero, por favor: '))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f'La raiz cuadrada de {numero} es: {solucion}')