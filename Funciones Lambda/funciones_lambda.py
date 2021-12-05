#------Funciones lambda------
#Es una funcion anonima, y se usa para abreviar (resume una funcion normal)
#Todo lo que se puede hacer con una funcion lambda se puede hacer en una funcion pero no al reves

#Ejemplo
"""def area_triangulo(base,altura):
    return (base * altura)/2"""

#Aqui nos viene bien las lambda porque es una funcion sencilla (Todas las funciones sencillas)

#Para la lambda es asi:
areaTriangulo = lambda base,altura:(base*altura)/2

triangulo1 = areaTriangulo(7,5)
triangulo2 = areaTriangulo(5,4)

print(triangulo1)
print(triangulo2)

al_cubo = lambda numero: pow(numero,3)
al_cubo2 = lambda numero: numero**3
print(al_cubo(13))
print(al_cubo2(13))

destacar = lambda comision: f"$// ¡{comision}!"
comision_David = 3000
print(destacar(comision_David))