#numeropar.py
print("Programa para saber si un numero entero es par o impar")
print("Ingrese un numero entero: ")
# int(cadena) numero entero Ej: int("3") 3; int("51.84") 50
numero = int(input())
# estructura selectiva si
if (numero % 2 == 0):   #Si num MOD 2 Entonces
    print (numero, " es par")
else: #SiNo
    print (numero, " es impar")




