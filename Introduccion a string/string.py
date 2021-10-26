#Strings
#Son secuencias de datos que las puedes usar para escribir texto
#y se identifican porque estan en comillas dobles o simples

nombre = "David" #Este es un ejemplo de string que esta guardado en una variable
apellidos = "Castillo" #las variables son espacios en memorias que almacenan un datos
fullname = nombre + apellidos
print(f"{nombre} {apellidos}") #para concatenar

#los strings son inmutables osea que no se pueden modificar una vez creadas
#algunos metodos para acceder a las secuencias son:

print(len(nombre)) #Indica cuantos elementos tiene el string (cuenta los espacions tambien)
print(f"El total de elementos del string es {len(nombre)}")
print(nombre[1]) #accede al elemento del indice que esta en el parametro
print(nombre[0:2]) #la secuencia comenzara desde 0 y termina en 2 (indices)
print(nombre*5) #lo repite 5 veces

print(nombre.find('i')) #busca de los indices de los parametros
nombre2 = nombre.replace("i","o") #reemplaza el elemento de la izquiera por el de la derecha
print(nombre2)
print(fullname.split(',')) #divide el string y los hace una lista
print(nombre.upper()) #los pasa a  mayusculas
print(nombre.lower()) #los pasa a minuscula

print('Hola gente que tal \n soy david')

