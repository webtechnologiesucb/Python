#ciclonaturales.py
print("Programa para generar los primeros n numeros naturales")
print("Ingrese la cantidad de numeros a mostrar: ")
n = int(input())
contador = 1
# Mientras contador <= n Hasta ...
while (contador <= n):
    print(contador, end=' ') # ' obligatorio
    contador = contador + 1
print("\n") # alt + 92  salto de linea
print("Fin del programa")
