# Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
var1=int(input("introduce un numero "))
var2=int(input("introduce otro numero "))

if var1<var2:
    print(f"el numero mas grande es {var2}")
elif var1>var2:
    print(f"el numero mas grande es {var1}")
else:
    print("los dos numeros son iguales ")
