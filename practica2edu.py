#calcular en base a un valor dado por el usuario
#su equivalencia en las diferentes divisas definidas

yuan=2.81
yen=0.13
dolar=20.54
euro=21.29
libra=25.56

pesos = input("ingresa la cantidad de pesos a convertir: ")

pesos = int(pesos)

print("tus pesos son %.2f yuanes" %(pesos/yuan))

print("tus pesos son %.2f yenes" %(pesos/yen))

print("tus pesos son %.2f dolares" %(pesos/dolar))

print("tus pesos son %.2f euros" %(pesos/euro))

print("tus pesos son %.2f libras" %(pesos/libra))