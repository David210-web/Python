#Veremos como se puede usar mas a fondo el bucle FOR
#Tipo range y notaciones especiales con print

#tipo range
for i in range(10): #comienza desde el cero asi que seria del 0 al 9
    print(f"valor de la variable: {i}")

#tambien admite otras notaciones por ejemplo
for i in range(1,10):
    print(f'Valor de la variable {i}')

#La funcion range admite 3 parametros
#1°Cantidad desde donde comenzamos a recorrer
#2°Cantidad hacia donde queremos que pare
#3°De cuanto en cuanto queremos contar (de 2 en 2 o de 3 en 3)

for i in range(1,100,10): #No será la mayoria de las veces pero se usa
    print(f"Valor de la variable {i}")

#tambien podemos recorrerlo con la funcion len():
valido = False
email = input('Introduce tu email: ')

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("El email es correcto")
else:
    print('Email incorrecto')