#Operadores logicos and, for e in en los condicionales
edad = 15

if 0<edad<100: #Se lee asi: 0 menor que edad y la edad menor que 100
    print("Edad es correcta")
else:
    print('Edad incorrecta')

print("----Evaluando salarios----")
salario_presidente = int(input('Introduce salario del presidente: '))
print(f'El salario es ${salario_presidente}') #tambien puedes usar la funcion str() para concatenar numeros

salario_director = int(input('Introduce salario del director: '))
print(f'El salario es ${salario_director}')

salario_jefe_area = int(input('Introduce salario del jefe de area: '))
print(f'El salario es ${salario_jefe_area}')

salario_administrativo = int(input('Introduce salario del director administrativo: '))
print(f'El salario es ${salario_administrativo}')

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print('Todo funciona correctamente')
else:
    print('Aqui hay truño en esta empresa')