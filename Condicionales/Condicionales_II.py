print('-------Verificacion de acceso-------')

edad_usuario = int(input('Introduce tu edad, por favor: '))

if edad_usuario < 18:
    print('Eres menor de edad no puedes pasar')
else:
    print('Eres mayor de edad puedes pasar')