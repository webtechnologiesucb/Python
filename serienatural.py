#serienatural.py
#Programa para imprimir los primeros n numeros naturales
print("Programa para imprimir los primeros n numeros naturales")
n = int(input("Ingrese la cantidad de terminos a imprimir: "))
contador = 1
# ciclo condicional mientras (while)
while (contador <= n):
    print(contador,end=' ')
    contador = contador + 1

print("Fin del programa")
