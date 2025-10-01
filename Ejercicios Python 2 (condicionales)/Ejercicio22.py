#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
var1=int(input(" introduce una nota "))

if var1<5:
    print(f"has suspendido")
elif var1>5:
    print(f"has aprobado")