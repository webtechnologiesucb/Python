# hipoteca.py
# Programa para realizar una hipoteca a un bien inmueble
print("Programa para realizar una hipoteca a un bien inmueble")
montoHip = eval(input("Ingrese el monto de hipoteca de la casa: "))
# estructura selectiva
if (montoHip < 1000000): # Si ... Entonces V
    print("El monto es menor a 1.000.000 Bs.")
    print("El cliente debe invertir ", montoHip * 50 /100)
else:                       # Sino  F
    print("El monto es mayor o igual a 1.000.000 Bs.")
    print("El cliente debe invertir ", montoHip)
