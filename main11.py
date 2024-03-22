# celsius.py
print('Programa para convertir de grados °C a °F')
print('Ingrese la temperatura en °C: ')
# input() recibir un texto desde el teclado
# eval(texto) convertir el texto en un numero real
gradosC = eval(input())
gradosF = (9/5) * gradosC + 32
print('La temperatura en °F: ', gradosF)
# probar con 0, 40, -40
