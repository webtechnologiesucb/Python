#programa03.py
import math

print("Programa para las operaciones entre dos numeros")
print("Ingrese el numero 1: ")
a = float(input())
print("Ingrese el numero 2: ")
b = float(input())
print("Suma: ", a + b)
print("Resta: ", a - b)
print("Multiplicacion: ", a * b)
if b == 0:
    print("Division: ", math.inf) # float('inf')
else:
    print("Division: ", a / b)
