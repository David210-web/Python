import re
cadena = "Vamos a aprender sobre expresiones regulares"
print(re.search("aprender",cadena))

if re.search("aprender",cadena) is not None:
    print("There´s a coincidence")
else:
    print("There´s not a coincidence")

textoBuscar = "aprender"
textoEncontrado = re.search(textoBuscar,cadena)

print(textoEncontrado.start()) #Donde comienza
print(textoEncontrado.end()) #Donde termina
print(textoEncontrado.span()) #Una cadena con las dos anteriores

cadena2 = "Vamos a aprender python. python es un lenguaje de sintaxis sencilla"
stringBuscado = "python" #Es keysensitive diferencia mayuscula y minuscula
print(re.findall(stringBuscado,cadena2))
print(len(re.findall(stringBuscado,cadena2)))
