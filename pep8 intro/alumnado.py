#alumnado.py
#En este programa insertaremos la información de vrios alumnos.
#Y la introduciremos en un archivo de texto que las recopile.
class MisAlumnos:
        # Escribe un mensaje en un fichero
    def escribe_fichero(self,mensaje):
        with open('fichero_comunicacion.txt', 'a') as fichero:
            fichero.write(mensaje)

    # Leer el mensaje del fichero        
    def lee_fichero(self):
        mensaje = ""
        with open('fichero_comunicacion.txt', 'r') as fichero:
            mensaje = fichero.read()
        # Manda lo intoducido al archivo de texto
        f = open('fichero_comunicacion.txt', 'a')
        f.close()
        return mensaje
    
alumno = MisAlumnos()
alumno.escribe_fichero("\n")
alumno.escribe_fichero(input("Ingresa tu edad: "))
alumno.escribe_fichero(", ")
alumno.escribe_fichero(input("Ingresa tu Año de nacimiento: "))
alumno.escribe_fichero(", ")
alumno.escribe_fichero(input("Ingresa tu Nombre: "))
alumno.escribe_fichero(".")
print(alumno.lee_fichero())
 #Actividad 3
 #parcial 2
