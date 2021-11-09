#importamos el modulo
import pickle


#creamos lo que queremos enviar
datos_persona = {
    "nombre":"David",
    "apellido":"Castillo",
    "edad":19,
    "ocupacion":"programador",
    "nacionalidad":"Salvadoreño"
}

#para enviarlos
archivo_enviar = open('datos persona','wb')
pickle.dump(datos_persona,archivo_enviar)
archivo_enviar.close()

#Para leerlos
archivo_recibir = open('datos persona','rb')
objeto_recibido = pickle.load(archivo_recibir)
archivo_recibir.close()
print(objeto_recibido)
datos = f"Objeto recibido.. \nNombre: {datos_persona['nombre']}\n" \
        f"Apellido: {datos_persona['apellido'] }\n" \
        f"Edad: {datos_persona['edad'] }\n"

print(datos)