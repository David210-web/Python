#Ultima parte de los bucles
#Continue, pass y else

#Continue: salta a la siguiente itereaccion del bucle
#Ejemplo un bucle que da 10 vueltas y en la vuelta 5 lee la instruccion
#pues ignora esa vuelta y salta a la otra

#pass: devuelve null (cuando se ejecuta el bucle) es poco comun y se usa para definir clases
#o para dejar para despues el desarrollo de un bucle

#else: funciona similar al del condicional

#Ejemplo

for letra in "Python":
    if letra == "h": #cuando se cumpla ignorará la palabra "H" en el prinit
        continue
    print(f"Viendo la letra {letra}")

#Utilidades
#Quiero contar el numero de caracteres y esta tiene espacios y quiero que los codigos no se cuenten
#entonces vamos a contar cuando caracteres tiene pero sin espacios
nombre = 'Pildoras informaticas'
contador = 0

for i in nombre:
    if i == ' ':
        continue
    contador += 1

print(contador)

#INSTRUCCION PASS
#Casos
#para bucles con while true o
#class MiClase:
 #   pass

#instruccion else
#Eh no es tan necesaria (#Se usa en for y en while) y se usa si el bucle este vacio

correo = input('Inserte tu correo electronico: ')

for i in correo:
    if i == "@":
        arroba = True
        print(arroba)
        break
else:
    arroba = False
    print(arroba)