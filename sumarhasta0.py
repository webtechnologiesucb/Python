#sumarhasta0.py
print("Programa para sumar n valores hasta 0")
suma = 0

while True:
    print("Ingrese un numero: ")
    numero = eval(input())
    if (numero == 0):
        break
    suma = numero + suma
print("La suma es: ", suma)
