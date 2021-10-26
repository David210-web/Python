x = 4
y = 5
z = 1.50
a = True

#Type nos sirve para saber que tipo de datos es un objeto, ejemplo
print(type(x)) #es de la clase int (entera)
print(type(z)) #float(decimal)
print(type(a)) #booelano

#las operaciones aritmeticas se ejecutan como en la vida real
print(x+y*3) #primero resuelve el porcentaje (o resuelve los parentesis si tiene)

#operaciones ya construidas por python
print(int(z)) #convierte cualquier dato a numerico (que tenga numero)
print(float(3)) #lo convierte a float


#-------Displa numerico-------------

num = 1/3.0
print(num)
print('%e' % num) #para pasarlo a formato exponencial
print('%4.2f'%num)


#-----Comparaciones-----------
print(1<3)