#Instruccion IF
nota_alumno = int(input('Ingresa la nota del alumno: '))

def evaluacion(nota):
    if nota > 5 and nota <= 10:
        print('Has sido aprobado')
    elif nota <= 10:
        print('Ingresa una nota valida')
    else:
        print('Has sido reprobado')

evaluacion(nota_alumno)

