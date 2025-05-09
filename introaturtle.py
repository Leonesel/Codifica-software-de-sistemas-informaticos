import turtle 
class TurtleForNoobs:
#Cuadrado 
    def test(self):
        skk = turtle.Turtle()
        for i in range(4):
            skk.forward(50)
            skk.right(90)
        turtle.done()

#Estrella
    def estrella(self):
        est=turtle.Turtle()
        est.right(75)
        est.forward(100)
        for i in range(16):
            est.right(144)
            est.forward(100)
        turtle.done()

#Circulo
    def circulo(self):
        est=turtle.Turtle()
        est.right(100)
        est.forward(10)
        for i in range(25):
            est.right(14.4)
            est.forward(30)
        turtle.done()

#Curva
    def curva(self):
        est=turtle.Turtle()
        est.right(75)
        est.forward(100)
        for i in range(8):
            est.right(14.4)
            est.forward(10)
        turtle.done()

#Puntero ue gira
    def puntero(self):
        est=turtle.Turtle()
        est.right(100000000)
        est.forward(10)
        for i in range(25):
            est.right(14.4)
            est.forward(30)
        turtle.done()

#Puntero que gira y crea una linea
    def lineapuntor(self):
        skk = turtle.Turtle()
        for i in range(4):
            skk.forward(100)
            skk.right(900)
        turtle.done()

t=TurtleForNoobs()
t.puntero()
#pip install PythonTurtle para instalar turtle