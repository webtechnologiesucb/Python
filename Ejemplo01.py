#Ejemplo01.py
# Para probar presionar F5
print("Programa para generar los N primeros numeros primos")
n = int(input("Ingrese la cantidad de terminos:"))
contador = 1
numero = 1
divisor = 1
while (contador <= n): # Mientras el contador sea menor a n
    contPrimo = 0 # inicia contador de divisores en 0
    while (divisor <= numero): # Mientras el divisor sea menor a num
        if (numero % divisor == 0):  # Si divisor es divisible
            contPrimo = contPrimo + 1
        divisor = divisor + 1
    # Fin del ciclo usando tabulador y sangria
    if(contPrimo == 2): # Si tiene dos divisores es primo
        print(numero, end=' ')
        contador = contador + 1 # incrementamos el contador
    divisor = 1 # divisor vuelve a 1
    numero = numero + 1 #incrementamos al siguiente numero
# Fin del ciclo usando tabulador y sangria
# \n es salto de linea
print("\nFin del programa")
