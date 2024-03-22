# Archivo: caos.py
# Un simple programa que ilustra un comportamiento caotico
print("Programa que ilustra un comportamiento caotico")
# input
# input(texto) para recibir valores de teclado como cadenas de texto
# eval(cadena) convierte un texto a valor numerico decimal
x = eval(input("Entre un numero entre 0 y 1: "))
# output
# for (para)
# for variable en rango (10): 0 - 9
for i in range(10):
    x = 3.9 * x * (1 - x)
    print("i=",i," ",end=' ')
    print("x=",x)

# print(val1, val2, end=enter)

