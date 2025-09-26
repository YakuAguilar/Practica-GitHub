#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal
import math
var1=float(input("introduce el diametro de un circulo "))
redondeo1=round(((var1/2)**2)*math.pi, 1)
print(f"el area del circulo es {redondeo1}")
redondeo2=round(var1*math.pi, 1)
print(f"el perimetro del circulo es {redondeo2}")