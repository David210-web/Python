archivo = open('datos.txt','w')
archivo.write('Estoy escribiendo con python en archivo en txt')
archivo.close()

leer = open('datos.txt','r')
txt = leer.read()
print(txt)
