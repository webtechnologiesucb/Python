# Comentarios cortos
# celsius.py
""" comentarios
largos del
desarrollador """
print("Programa para convertir °C a °F")
# definir variables
gradosC = 0
gradosF = 0
# input(mensaje) recibe cadenas de texto
# eval(cadena) convierte los textos a numeros
gradosC = eval(input("Ingrese temperatura °C: "))
# aplicamos la formula
gradosF = (9/5) * gradosC + 32
# output
print("La temperatura en °F es: ", gradosF)

