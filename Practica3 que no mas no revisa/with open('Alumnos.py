with open('Alumnos.txt', 'r') as ficheros:
    for linea in ficheros:
        print(linea, end='')

fichero = open("Alumnos.txt", 'w')
lista = ["11- Adoño Lopez Luis Angel\n", "12- Angeles Hernandez Alan Dwii\n", "13- Diaz Nuñes Kevin Aaron\n","14- Garcia Guzman Andrea Guadalupe\n", "15- Garcia Herrrera David Iyari\n", "16- Gomez Fernandez Jose Roberto\n","17- Gonzales Jacinto Michelle Estefania\n", "18- Mejia Lopez Angel Gadiel\n", "19- Jimenes Job Esau\n","20- Rios Garcia Angel Abraham\n"]

fichero.writelines(lista)
fichero.close()