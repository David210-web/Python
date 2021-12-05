#--Funcion filter--
def numero_par(num):
    if num%2 == 0:
        return True

numeros = [17,22,34,65,80]
print(list(filter(numero_par,numeros)))

print(list(filter(lambda numeroPar: numeroPar%2 ==0,numeros)))

#Para filtrar objetos
class Empleados:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre,
        self.cargo = cargo,
        self.salario = salario
    def __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de {self.salario}$"

listaEmpleados = [
    Empleados("David","Gerente",7500),
    Empleados("Karla","Administradora",8500),
    Empleados("Jun","Secretaria",25000),
    Empleados("Mario","Tesorero",27000),
    Empleados("Yagami","Empleado",3500),
]

salarios_altos = filter(lambda empleado: empleado.salario > 10000,listaEmpleados)
for salario in salarios_altos:
    print(salario)