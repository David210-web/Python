#Expresiones regulares III
#Rangos
import re

nombres = ["Ana","Maria","Pedro","Rosa","Sandra","Cecicilia"]
for nombre in nombres:
    if re.findall('[e-h]',nombre): #Buscar un rango desde la letra E hasta la H
        print(nombre)

print("---------------------------------------")

for nombre in nombres: #Podemos usar rangos con ^ y $
    if re.findall('[^e-h]',nombre): #Buscar un rango desde la letra E hasta la H
        print(nombre)

print("---------------------------------------")

#Para leer codigos
codigos = ["sv1","sa1","sm1","sv2","sv3","sv4","sm2","lpz1","sv5"]
codigos2 = ["sv1","sa1","sm.1","sv2","sv3","sv4","sm.2","lpz1","sv5"]
for codigo in codigos:
    if re.findall("sv[1-3]",codigo):
        print(codigo)

print("---------------------------------------")

#Para hacer rangos inversos (que los que estan de parametro sea los que no cuenten)
for codigo in codigos:
    if re.findall("sv[^1-3]",codigo):
        print(codigo)

print("---------------------------------------")
#Doble rango
for codigo in codigos:
    if re.findall("sv[^1-3A-B]",codigo):
        print(codigo)
    else:
        print("No se ha encontrado la condicion")


#Con signos de puntuacion
print("---------------------------------------")
for codigo in codigos2:
    if re.findall("sm[:.]",codigos2):
        print(codigo)


print("-------Ejecucion terminada-------")