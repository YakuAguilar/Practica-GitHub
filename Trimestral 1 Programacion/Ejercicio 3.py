

positivos=0
n_cifras=int(input("dime cuantas cifras quieres introducir "))
for x in range(n_cifras):
    var1=float(input("introduce un numero "))
    positivos=positivos+var1
print(f"la suma total de los positivos es: {positivos}")