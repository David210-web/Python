#Ejercicio Final
print('Asignaturas optativas Año 2022')
asignaturas = ["Informatica grafica",'Pruebas de software','Usabilidad y accesibilidad']
print(f"las materias son: {asignaturas[0]} - {asignaturas[1]} - {asignaturas[2]}")

asignatura = input('Escribe la materia escogida: ')

if asignatura in asignaturas:
    print(f'Asignatura elegida: {asignatura}')
else:
    print('La asignatura escogida no esta contemplada')

#tambien la podemos hacer de este modo
if asignatura in ("Informatica grafica",'Pruebas de software','Usabilidad y accesibilidad'):
    print(f'Has elegido: {asignatura}')
else:
    print('La materia escogida no está contemplada')