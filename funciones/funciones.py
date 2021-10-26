#sintaxis

#sin parametros
def nombreFuncion():
    dato = input('Dime tu nombre: ')
    return f"Hola {dato}" #El return es completamente opcional


print(nombreFuncion())

#con parametros
dato1 = int(input('Dime un numero: '))
dato2 = int(input('Dime otro numero: '))
def suma(a,b):
    print(f"El resultado es: {a + b}")

suma(dato1,dato2) #pero puede recibir muchos parametros e iran separados por coma