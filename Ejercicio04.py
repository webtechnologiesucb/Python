#Ejercicio04.py
print("Programa para obtener la cantidad de digitos de un numero")
n = int(input("Ingrese un numero entero: "))
contDigitos = 0 #conteo de digitos
aux = n #guardo el numero
while(n>0): # mientras n sea un numero diferente de cero
    contDigitos = contDigitos + 1 # cuento digitos
    n = n // 10 # divido para seguir contando
print("La cantidad de digitos de", aux, "es: ", contDigitos)
