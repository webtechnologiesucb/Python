#interessec.py
#Programa para calcular el interes mensual de un deposito
print("Programa para calcular el interes mensual de un deposito")
#definimos valores iniciales
deposito = 0.0
interes = 2
interesGanado = 0.0
#solicitamos el ingreso de valores
deposito = eval(input("Ingrese el monto depositado: ")) # ingreso el monto
# proceso
interes = interes / 100 # convierto interes a decimal porcentaje
interesGanado = interes * deposito # aplico formula
# mostrar el resultado
print("Interes ganado: ", deposito + interesGanado) # imprimo resultados

