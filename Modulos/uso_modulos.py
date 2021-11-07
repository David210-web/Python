#si quieres usar un modulo en python lo primero que debes hacer es
#usar la palabra reservada python

import modulos
#para ejecutar la funcion, primero llamamos al modulo y usamos la nomenclatura del punto
#para llamar a las funciones que estan ahi
modulos.sumar(6,2)
modulos.restar(4,2)

#pero si no queremos escribir el modulo delante de la funcion sera asi:

from modulo_prueba2 import *
#esto dice que queremos importar todas las funciones (por eso el *)
#del archivo modulo_prueba2 (si quieres importar solo una funcion pues
# entonces solo deberias poner el nombre de la funcion que queres ejecutar)
sumar(2,2)
restar(5,3)
multiplicar(3,2)

#En programas grande no deberias usar el * porque usaras mucho espacio en memoria
#mejor solo usa el nombre de la clase para que no almacene espacio en memoria
