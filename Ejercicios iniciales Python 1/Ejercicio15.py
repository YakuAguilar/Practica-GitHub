# Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
var1=float(input("introduce la altura de un cilindro "))
var2=float(input("introduce el radio de un cilindro "))
redondeo1=round(((2*math.pi*(var2**2))+2*math.pi*var2*var1), 2)
print(f"el area del circulo es {redondeo1}")
redondeo2=round(math.pi*(var2**2)*var1, 2)
print(f"el volumen del circulo es {redondeo2}")