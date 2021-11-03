#super() e instance()
#En el codigo pasado vimos que cuando hay herencia multiple se dará prioridad al primero
#asi que en caso que VElectricos y vehiculos tenga metodos con el mismo nombre la clase
#BicicletaElectrica utilizara los metodos de VElectricos (clases vistas en POO_V.py)
#en este caso usara el metodo init de VEelectricos porque le da preferencia

#1-Irnos a la clase VElectrico y en su constructor repetir la construccion (Marca y  modelo)
#esta es una forma no eleganta

#2-La funcion elegante pasar por usar la funcion super(),esta funcion allá donde la coloques en tu codigo
#va a llamar al metodo de la clase padre

#Ejemplo con super()
class Persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print(
            f"Nombre: {self.nombre}, "
            f"Edad: {self.edad}, "
            f"Residencia: {self.lugar_residencia}"
        )

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        #super().__init__('Lucas',20,'El Salvador') #Para valores fijos
        #Nos sirve para llamar al metodo init de la clase padre por eso el nombre,edad y residencia
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado) #Para que el usuario ponga el metodo
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        #Lo que hace aqui la opcion super es: primero manda a traer el metodo descripcion de la clase padre
        #para que se ejecute en el metodo descripcion de esta clase y asi podemos agregarles
        #codigo extra a el metodo de la otra clase pero en esta clase
        print(f"Salario: {self.salario}, Antiguedad: {self.antiguedad}")

David = Persona('David',20,'El Salvador')
David.descripcion()

Lucas = Empleado(1500,'2 años','Lucas',32,'Guatemala')
Lucas.descripcion() #Pero esto daria error porque el constructor empleado no nos deja poner nombre

#Cuando estamos trabajando con herencia cuando trabajamos con muchas clases llega un momento en que uno
#a la hora de construir una instancia debido a la herencia no sabe si realmente pertenece a una clase
#o pertenece a otra

#Cuando se trabaja con la herencia existe algo que se llama principio de sustitucion esto consiste en
#aplicar los terminos de "Es siempre un/una" cuando tenemos herencia un objeto de la subclase siempre
#sera un objeto de la super clase (Un empleado es siempre una persona, al reves esto es imposible porque
# por ejemplo una persona puede no ser un empleado o no tener un trabajo) esto tambien se usa tambien
#para comprobar que un diseño de herencia es correcto o esta bien creado, en python tenemos
#la funcion isinstance() que nos informa si un objeto es instancia de una clase determinada

#por ejemplo Lucas (El objeto) debe ser parte de la clase Persona (Devolvera True o False)

print(isinstance(Lucas,Empleado)) #El primer parametro es donde esta guardado el objeto (El nombre)
#y el segundo la clase donde pertence

#Pero ahora vamos a comprobar si es de tipo Persona debido al principio de sustitucion deberia serlo
print(isinstance(Lucas,Persona)) #Aqui saldra true porque es empleado y persona
print(isinstance(David,Empleado))