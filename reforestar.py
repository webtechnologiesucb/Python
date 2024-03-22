#reforestar.py
#Programa para analizar el reforestamiento de un bosque
print("Programa para analizar el reforestamiento de un bosque")
totalHa = eval(input("Ingrese el total de Ha del terreno:"))
if(totalHa * 10000 > 1000000):
    print("Ha Pino: ", totalHa * 70 / 100)
    print("Ha Fresno: ", totalHa * 20 / 100)
    print("Ha Cedro: ", totalHa * 10 / 100)

