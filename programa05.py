#programa05.py
print("Programa para imprimir los primeros N numeros naturales")
print("Ingrese un numero natural: ")
numero = int(input())
contador = 1
while contador <= numero:
    print(contador, end=' ')
    contador = contador + 1
print("Fin del programa")
