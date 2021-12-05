import re
#Anclas
lista_nombres = ["David Castillo","Cosme Fulanito","Nicolas Tranquilino","Christian Castillo"]
for nombre in lista_nombres:
    if re.findall('^David',nombre):
        print(nombre)
    if re.findall('Castillo$',nombre):
        print(nombre)

lista_dominios = ['http://pildorasInformaticas.es','ftp://pildorasinformaticas.es','http://pildorasinformaticas.com','ftp://pildorasinformaticas.com']

for dominio in lista_dominios:
    if re.findall("com$",dominio):
        print(dominio)

print("--------------------------")

for dominio in lista_dominios:
    if re.findall("^http",dominio):
        print(dominio)

print("----------------------------")

#Clases de caracteres
ista_dominios = ['http://informaticaenespaña.es','http://pildorasInformaticas.es','http://pildorasInformaticas.com']
for dominio in ista_dominios:
    if re.findall('[ñ]',dominio):
        print(dominio)

print("---------------------------")

lista_nombres2= ['hombres','mujeres','mascotas','niños','niñas']
for nombre in lista_nombres2:
    if re.findall('niñ[aeo]',nombre):
        print(nombre)


nombre1 = "Salah"
nombre2 = "Pedri"
nombre3 = "Cristiano"
nombre4 = "Mariano"
nombres = [nombre1,nombre2,nombre3,nombre4]
for nombre in nombres:
    if re.findall('[e]',nombre):
        print(nombre)