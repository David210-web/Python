nombreUsuario = 'David'
print(f"El nombre es {nombreUsuario}")

#Upper lower y capitalize
print(nombreUsuario.upper()) #Mayusculas
print(nombreUsuario.lower()) #Minusculas
print(nombreUsuario.capitalize()) #Primera letra en mayuscula

#Aplicabilidad practica
edad = input('Introduce la edad: ')
print(edad.isdigit())

while edad.isdigit() == False:
    print('Por favor introduce una edad valida')
    edad = input('Introduce tu edad: ')

if int(edad) < 18:
    print('Eres menor de edad, no puedes pasar')
else:
    print('Eres mayor de edad puedes pasar')