try:
    op1 = int(input('Introduce el primer numero: '))
    op2 = int(input('Introduce el segundo numero: '))
except ValueError:
    print('Los valores introducidos son incorrectos')

#Esta sentencia puede funcionar:
while True:
	try:
		op1 = int(input('Introduce el primer numero: '))
		op2 = int(input('Introduce el segundo numero: '))
		break
	except ValueError:
		print('Los valores introducidos no son correctos. Intentalo de nuevo')

#1-Podemos hacer esto:
def divide():
	try:
		op1= int(input("Introduce el primer numero: "))
		op2= int(input("Introduce el segundo numero: "))
		print('La division es: ' + str(op1/op2))
	except ValueError:
		print('Los valores introducidos no son correctos.')
	except ZeroDivisionError:
		print('No se puede dividir entre 0!')

#2-Tambien podemos capturar algo en general, pero es poco recomendable porque el usuario no sabra que paso
def divide2():
	try:
		op1= int(input("Introduce el primer numero: "))
		op2= int(input("Introduce el segundo numero: "))
		print('La division es: ' + str(op1/op2))
	except:
		print('Los valores introducidos no son correctos.')

#3-Cuando quieres que un codigo se ejecute siempre debemos meterlo dentro de una etiqueta finally

def divide3():
	try:
		op1= int(input("Introduce el primer numero: "))
		op2= int(input("Introduce el segundo numero: "))
		print('La division es: ' + str(op1/op2))
	except ValueError:
		print('Los valores introducidos no son correctos.')
	except ZeroDivisionError:
		print('No se puede dividir entre 0!')
	finally:
		print('Calculo finalizado')

#4-
def divide():
	try:
		op1= int(input("Introduce el primer numero: "))
		op2= int(input("Introduce el segundo numero: "))
		print('La division es: ' + str(op1/op2))
	finally:
		print('Calculo finalizado')