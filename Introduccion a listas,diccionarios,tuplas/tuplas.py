#Son como las listas pero son inmutables
datos = ('David','Castillo','Maruchan')
print(datos)
print(datos.index('Maruchan'))
print('David' in datos)

miLista = list(datos) #aqui la podemos pasar a lista
print(type(datos))
print(type(miLista))
miTupla = tuple(miLista) #aqui la lista la podemos pasar a tupla
print(type(miTupla))

print(miTupla.count('David')) #cuenta cuantas veces hay este dato

datoTupla = ("Juan",12,1,2002)
name,day,month,year = datoTupla #este es el desempaquetado de tuplas
print(name)