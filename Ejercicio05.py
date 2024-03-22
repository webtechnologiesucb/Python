#Ejercicio05.py
print("Programa para invertir los digitos de un numero")
n = int(input("Ingrese un numero entero: "))
aux = n # guardo el numero ingresado en otra variable
nuevoNumero = 0 # declaro el numero nuevo en cero
while(n>0):
    digito = n % 10 # extraigo el digito
    nuevoNumero = nuevoNumero * 10 + digito # genero el nuevo numero
    n = n // 10 # divido para obtener mas digitos
print("El inverso de", aux, "es: ", nuevoNumero)
