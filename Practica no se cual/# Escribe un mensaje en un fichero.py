import datetime


ant = []
acum = 0
con = 0
app = 1
with open("iteraciones.txt","r") as fichero:
    for linea in fichero.readlines():
        el=linea.split(",")

        if con > 0:
            if el[0] == ant[0]:
                fechAct = datetime.strptime(el[1].replace("\n",""), "%m/%d/%y/")
                fechAnt = datetime.strptime(ant[1].replace("\n",""), "%m/%d/%y/")
                dias = abs(fechAct-fechAnt).days
                acum += dias
                app = app +1
                print(fechAct," ",fechAnt," ",dias)
            else:
                print(ant[0],"",int(acum/app))
                acum=0
                app=0
        ant=el[:]
        con = con+1
        print(ant[0], "", int(acum/app))
