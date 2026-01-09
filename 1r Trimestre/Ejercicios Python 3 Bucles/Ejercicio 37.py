#Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.

numeroveces=int(input("introduce el numero de notas que quieres introducir "))
for i in range (numeroveces):
    nota= float(input("Introduce la nota : "))
    if nota<5:
        print(" suspendido")
    else:
        print("aprobado")


