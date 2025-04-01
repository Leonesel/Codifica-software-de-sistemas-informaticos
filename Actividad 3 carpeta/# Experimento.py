# Escribe un mensaje en un fichero
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'a') as fichero:
        fichero.write(mensaje)

# Leer el mensaje del fichero        
def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()

    # Borra el contenido del fichero para dejarlo vacío
    f = open('fichero_comunicacion.txt', 'a')
    f.close()
    return mensaje
escribe_fichero("\n")
escribe_fichero(input("Ingresa tu edad: "))
escribe_fichero(", ")
escribe_fichero(input("Ingresa tu Año de nacimiento: "))
escribe_fichero(", ")
escribe_fichero(input("Ingresa tu Nombre: "))
escribe_fichero(".")
print(lee_fichero())
#Actividad 3




