#Sintaxis:
#for variable in elemento a recorrer: (El elemento a recorrer puede ser una tupla,lista,cadena,etc)
#   cuerpo del bucle (Tiene que estar identado para que el for lo reconozca)
#   puede tener mas de una linea de codigo pero tiene que estar identada

for i in [1,2,3,4,5]: #el i recorre asi: i = 1, i = 2 y asi sucesivamente y este imprime el dato
    #y cuando ya no puede asignas mas valores el bucle se detiene
    print(f'El numero es: {i}')

estaciones = ['primavera','invierno','verano','otoño']
for estacion in estaciones:
    print(estacion)