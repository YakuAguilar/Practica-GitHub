
numeroveces=int(input("introduce el numero de notas que quieres introducir "))
for i in range (numeroveces):
    nota= float(input("Introduce la nota : "))
    if nota < 0 or nota > 10:
        print("Nota no válida, debe estar entre 0 y 10.")
    elif nota<5:
        print(" suspendido")
    else:
        print("aprobado")
    
