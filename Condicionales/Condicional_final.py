#AND, OR E IN
print('----Programa de derecho a beca----')
distancia_escuela = int(input('Introduce la distancia en KM: '))
print(f'El total es: {distancia_escuela}')

numeros_hermanos = int(input('Introduce la cantidad de hermanos: '))
print(f'El total es: {numeros_hermanos}')

salario_familiar = int(input('Introduce el salario anual bruto: '))
print(f"El salario es: {salario_familiar}")

if distancia_escuela > 40 and numeros_hermanos > 2 or salario_familiar <= 20000:
    print('Felicidades tienes derecho a Beca')
else:
    print('No tiene derecho a Beca')