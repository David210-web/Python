#Guardar informacion de forma permanente en ficheros externos haciendo lo visto anteriormente
import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f'Se ha creado una persona nueva con el nombre de {self.nombre}')

    def __str__(self): #convierte en string la info de un objeto
        return f"{self.nombre} {self.genero} {self.edad}"


class ListaPersona:
    personas = []
    def __init__(self):
        listaDePersonas = open('ficheroExterno','ab+')
        listaDePersonas.seek(0)
        try:
            self.personas = pickle.load(listaDePersonas)
            print(f'Se cargaron: {len(self.personas)} del fichero externo')
        except:
            print('El fichero esta vacio')
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self,per):
        self.personas.append(per)
        self.guardarPersonas()

    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)

    def guardarPersonas(self):
        listaDePersonas = open('ficheroExterno','wb')
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfo(self):
        print('La informacion del fichero es la siguiente: \n')
        for per in self.personas:
            print(per)


lista = ListaPersona()
persona1 = Persona('Ana','Femenino',21)
lista.agregarPersonas(persona1)
lista.mostrarInfo()
#p = Persona('David','Maculino',23)
#p2 = Persona('Karla','Femenino',23)
#p3 = Persona('Juan','Desconocido',27)

#lista.agregarPersonas(p)
#lista.agregarPersonas(p2)
#lista.agregarPersonas(p3)
#lista.mostrarPersonas()
#crear personas y almacenarlas en un archivo externo
#y para almacenar informacion:
