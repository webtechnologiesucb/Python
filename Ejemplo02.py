# Ejemplo02.py
# Para probar presionar F5
print("Programa para generar los N primeros numeros perfectos")
n = int(input("Ingrese la cantidad de terminos:"))
contador = 1
numero = 1
divisor = 1
while (contador <= n): # Mientras el contador sea menor a n
    sumaPerfecto = 0 # inicia sumador de divisores en 0
    while (divisor <= (numero/2)): # Mientras el divisor sea menor a num
        if (numero % divisor == 0):  # Si divisor es divisible
            sumaPerfecto = sumaPerfecto + divisor # suma el divisor
        divisor = divisor + 1
    # Fin del ciclo usando tabulador y sangria
    if(sumaPerfecto == numero): # Si es igual al numero es perfecto
        print(numero, end=' ')
        contador = contador + 1 # incrementamos el contador
    divisor = 1 # divisor vuelve a 1
    numero = numero + 1 #incrementamos al siguiente numero
# Fin del ciclo usando tabulador y sangria
# \n es salto de linea
print("\nFin del programa")
