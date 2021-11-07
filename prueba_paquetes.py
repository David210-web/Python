#Este archivo esta relacionado con la carpeta paquetes
from Paquetes.calculos_generales import *

sumar(2,2)
restar(3,2)
multiplicar(3,3)
dividir(15,3)
potencia(30,2)
redondear(3.43)

#Podemos crear subpaquetes un paquete dentro de otro
#una carpeta adentro de la carpteta Paquetes que se llame
#basicos (calculos basicos) avanzados (Calculos avanzados) y ahi almacenar datos pero todo deben llevar
#el archivo __init__.py

#y para usar es: from Paquetes.basicos.operaciones_basicas import *
#las primeras dos es La carpeta principal y la otra la subcarpeta y la tercera es el archivo