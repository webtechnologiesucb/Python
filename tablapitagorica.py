#tablapitagorica.py
print("Programa para generar la tabla pitagorica de multiplicar")
a = 1
while (a<=10):       #MIENTRAS
    b = 1
    while (b<=10):   #MIENTRAS
        if (b!=10):  #SI
            print(a*b, end='\t')
        else:        #SINO
            print(a*b)
        b = b + 1
    print("\n") # ALT + 92
    a = a + 1

print("\nFin del programa")
