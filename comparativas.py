#comparativas.py
x = 5
# Estructura selectiva
if (x < 5):  # Si x < 5 Entonces
    print("Menor valor") # Imprimir "Menor Valor"
else: # SiNo
    print("Mayor valor") # Imprimir "Mayor Valor"
# FinSi

cont = 0 # contador de ciclo
suma = 0 # suma de ciclo
while(cont <= x): # Mientras cont <= x Hacer
    suma = suma + cont
    cont = cont + 1
# FinMientras
print("Suma: ", suma) # Imprimir "Suma: ", suma

# Ciclo Para
for i in range(1,7,1): # Para i=1 Hasta 6 Con Paso 1 Hacer
    print(i)# Imprimir i
# Fin Para

# Ciclo HastaQue
while True: # Repetir
    print("Ingrese un numero") # Imprimir "Ingrese un numero: "
    n = int(input()) # leer n
    if n==0:
        break
# Hasta Que n=0
# Segun ... Hacer
print("MENU DE OPCIONES") # Imprimir "MENU DE OPCIONES"
print("1. INGRESE NUMERO") # Imprimir "1. INGRESE NUMERO"
print("2. SUMAR NUMEROS ENTEROS") # Imprimir "2. SUMAR NUMEROS ENTEROS"
print("3. DIVIDIR NUMEROS") # Imprimir "3. DIVIDIR NUMEROS"
print("4. SALIR") # Imprimir "4. SALIR"
print("ELIJA UNA OPCION") # Imprimir "ELIJA UNA OPCION"
opcion = int(input()) # Leer opc
match opcion: # Segun opc Hacer
    case 1: # 1:
        print("Eligio opcion 1") # Imprimir "Eligio opcion 1"
    case 2: # 2:
        print("Eligio opcion 2") # Imprimir "Eligio opcion 2"
    case 3: # 3:
        print("Eligio opcion 3") # Imprimir "Eligio opcion 3"
    case 4: # 4:
        print("Eligio opcion 4") # Imprimir "Eligio opcion 4 Salir"
    case _: # De Otro Modo:
        print("Opcion incorrecta") # Imprimir "Opcion incorrecta"
# Fin Segun
""" Comentario en linea multiple
Ingresa tus comentarios """
print("Fin del Programa")





    
