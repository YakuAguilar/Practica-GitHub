# Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
var1=float(input("introduce un numero "))
var2=float(input("introduce un numero "))
print(f"el cociente es {var1/var2}")
print(f"el resto es {var1%var2}")

if var1 % 2 == 0:
    print(f"el dividendo es par ")
else:
    print(f"el dividendo es impar ")



