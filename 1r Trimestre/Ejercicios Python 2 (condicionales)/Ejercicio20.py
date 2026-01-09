#. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=int(input("introduce un numero entre el 0-10 "))
var2=int(input("introduce otro numero entre 0-10 "))

if var1<0 or var1>10 or var2<0 or var2>10:
    print(f"uno de los 2 numero es mayor de 10 o menor de 0")
elif var1>var2:
    print(f"el numero mas grande es {var1}")
elif var1<var2:
    print(f"el numero mas grande es {var2}")
else:
    print("los dos numeros son iguales ")