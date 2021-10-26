#Sintaxis del bucle while
#Wile condicion a evaluar:
    #Cuerpo del bucle

#Es como un condicional

i = 1
while i <= 3:
    print(f"El valor de i es: {i}")
    i = i+1

print("Termino la ejecucion")

edad = int(input("Introduce la edad, por favor: "))
while edad < 5 or edad > 100:
    print("Has introducido una edad negativa, try again")
    edad = int(input("Introduce la edad, por favor: "))

print("Gracias por colaborar puedes pasar")
print(f"Edad del aspirante {edad}")

#tambien podemos usar los operadores
