#Son como las listas pero se ordenan por clasves y no por posicion

datos = {
    "nombre":"David",
    "edad": 18,
    "ocupacion": "estudiante"
}

print(datos["edad"])

datos["sexo"]="masculino" #agrega un dato nuevo
print(datos)

#tambien podemos crear uno vacio y despues llenarlo
datos2 = {}
datos2["nombre"]= "karla"
datos2["apellidos"]="clara"
print(datos2)

#Eliminar un elemento
del datos['edad'] #usamos el metodo del y ponemos la clave
print(datos)

#podemos usar una tupla como clave asi:
tupla = ('nombre','edad','ocupacion')
diccionario = {
    tupla[0]:'David',
    tupla[1]:18,
    tupla[2]:'Estudiante'
}

print(diccionario)

print(diccionario.keys())
print(diccionario.values())
print(len(diccionario))