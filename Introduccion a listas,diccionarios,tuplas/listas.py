#Es practicamente como un array y es mutable
lista = [1,2,"David","Carlos"]
print(lista)
print(f"{lista[1]}") #asi podemos acceder al indice
lista.append("Dato nuevo") #Agrega un nuevo dato
print(lista)
lista.pop() #elimina un dato
print(lista)
numeros = ["s","e","a"]
numeros.sort() #ordena una lista si es de un solo dato
print(numeros)

miLista = ["maria","pepe","marta","antonio"]
print(miLista.insert(2,'juan')) #agrega el dato a la posicion que queremos (en este caso 2)
print(miLista.extend(["david","karla","fernado"]))#para agregar varios elementos
print(miLista.index('marta')) #devuelve el indice del dato
print(miLista)
print('pepe' in miLista) #nos muestra si este dato se encuentra en la lista

miLista.remove('ana') #elimina el dato que esta como parametro
