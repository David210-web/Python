from io import open

#Para crear un archivo y escribir en el
archivo_write = open('escribir.txt','w')
frase = 'Que lindo dia para aprender python'
archivo_write.write(frase)
archivo_write.close()

#Para leer un archivo
archivo_read = open('escribir.txt','r')
texto = archivo_read.read()
archivo_read.close()
print(texto)

#Para leer lineas
archivo2 = open('escribir2.txt','w')
lineas = 'Estoy escribiendo \n, desde la consola \n de python.'
archivo2.write(lineas)
archivo2.close()

leerLineas = open('escribir2.txt','r')
lista = leerLineas.read()
leerLineas.close()

#para seguir escribiendo
sobreEscribir = open('escribir.txt','a')
frase = ' Sigo escribiendo en consola'
sobreEscribir.write(frase)