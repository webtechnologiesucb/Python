#comisionessec.py
#Programa para obtener comisiones para pago de sueldos y salarios
print("Programa para obtener comisiones para pago de sueldos y salarios")
#variables de entrada
#dinero -> float(texto) convierte en decimal
venta1 = float(input("Ingrese monto de venta 1:"))
venta2 = float(input("Ingrese monto de venta 2:"))
venta3 = float(input("Ingrese monto de venta 3:"))
sueldoMes = float(input("Ingrese su salario mensual:"))
#proceso
comision = (venta1 + venta2 + venta3) * (10/100)
# salida
print("El total ganado mas comisiones es", sueldoMes + comision)
