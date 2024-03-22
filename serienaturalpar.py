#serienaturalpar.py
#Programa para imprimir los primeros n numeros naturales pares
print("Programa para imprimir los primeros n numeros naturales pares")
n = int(input("Ingrese la cantidad de terminos a imprimir: "))
numero = 1 # sigue el ciclo normal
contador = 1 # cuenta los numeros pares
# ciclo condicional mientras (while)
while (contador <= n):
    if (numero % 2 == 0):
        print(numero,end=' ')
        contador = contador + 1
    numero = numero + 1

print("Fin del programa")
