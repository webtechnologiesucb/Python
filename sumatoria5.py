#sumatoria5.py
print("Programa para sumar los primeros n multiplos de 5")
print("Ingrese la cantidad de terminos a sumar: ")
n = eval(input())
cont = 1
suma = 0
valor = 0
while (cont <= n):
    valor = valor + 5
    suma = suma + valor
    cont = cont + 1
print("Suma: ", suma)
