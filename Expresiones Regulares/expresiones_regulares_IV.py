#Expresiones regulares IV
#Match y Search
import re

nombre1 = "David Lopez"
nombre2 = "Maria Lopez"
nombre3 = "Eduardo Lopez"
nombre3 = "Jose Juan"
nombre4 = "Bruno Diaz"
nombre5 = "Ricardo Tapia"
nombres = [nombre1,nombre2,nombre3,nombre4,nombre5]

#Buscar coincidencias al comienzo del texto
print("---------------Funcion Match---------------")
def coincidencia(coincidencia):
    if re.match("David",coincidencia,re.IGNORECASE):
        print(f"Se ha encontrado el dato: {coincidencia}")
    else:
        print("No se ha encontrada nada")

coincidencia(nombre1)
coincidencia(nombre2)

#Podemos usar un punto comodin solo para la primera letra asi
name1 = "Lara lopez"
name2 = "Sara lopez"
name3 = "Pancho lopez"

print("---------------Funcion 2---------------")

def coincidencia2(coincidencia):
    if re.match(".ara",coincidencia,re.IGNORECASE):
        print(f"Se ha encontrado el dato: {coincidencia}")
    else:
        print("No se ha encontrada nada")

coincidencia2(name1)
coincidencia2(name2)
coincidencia2(name3)

print("---------------Funcion 3---------------")

#Para buscar cadenas que empiezen con un numero
cadena1 = "5ahjdlkajdlkajl"
cadena2 = "a46542625626565"

def coincidencia3(coincidencia):
    if re.match("\d",coincidencia,re.IGNORECASE):
        print(f"Se ha encontrado el dato: {coincidencia}")
    else:
        print("No se ha encontrada nada")

coincidencia3(cadena1)
coincidencia3(cadena2)

print(("---------------Funcion Search---------------"))
#Es casi lo mismo que match pero busca en toda la cadena de texto para ver si se encuentra el patron
def coincidenciaSearch(coincidencia):
    if re.search("Lopez",coincidencia,re.IGNORECASE):
        print(f"Se ha encontrado el dato: {coincidencia}")
    else:
        print("No se ha encontrada nada")

coincidenciaSearch(nombre1)
coincidenciaSearch(nombre2)
coincidenciaSearch(nombre3)
coincidenciaSearch(nombre4)
coincidenciaSearch(nombre5)

print("----------Ejecucion finalizada----------")