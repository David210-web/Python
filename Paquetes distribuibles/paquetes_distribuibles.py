#sirve para que podamos llamar a un paquete independientemente donde estemos
#para eso instalaremos el paquete en nuestro windows para que el archivo lo pueda leer

#Se crea un archivo en la raiz llamado setup.py que contendra descripcion
#del paquete que vamos a distribuir asi:

from  setuptools import setup

setup(
    name='paquetecalculos',
    version='1.0',
    description='Paquete de paquetes distibuibles',
    author='David',
    #opcionales
    author_email='cdavidrigoberto@gmail.com',
    url='www.davidcastillo.sv',
    #y la mas importante que sirve para indicar donde se encuentra el paquete o subpaquetes que
    #queremos empaquetar
    packages=['calculos','calculos.redondeo_potencia']
)

#El siguiente paso es ir a la carpeta donde esta el setup y con esa direccion irnos al cmd
#(poner con cmd la direccion de carpetas de este archivo)
#y luego lo creamos como paquete distribuible asi:
#python setup.py sdlist y luego nos creara dos carpetas
#1-paquetecalculos.egg-info
#2-dist (es el mas importantes)
#en el dist encontraremos un archivo tar.gz (es un archivo comprimido) y los descomprimimos
#(o lo podemos enviar a alguien que lo quiera instalar por email ahi es tu decision)

#y para instalarlo sera adentro de la carpeta dist
#y en el cmd del directorio ponemos:
#pip3 install paquetecalculos-1.0.tar.gz
#y ahora podemos usar el paquete en cualquier direccion que este nuestro archivo

#y para desintalarlo ponemos: pip3 unistall paquetecalculos (no importa la direccion de carpetas)
#nos hara una preguntas pondremos Yes o si