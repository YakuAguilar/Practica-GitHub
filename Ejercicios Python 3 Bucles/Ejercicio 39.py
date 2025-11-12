
negativos=0
positivos=0
ceros=0
numeroveces=int(input("introduce el numero de notas que quieres introducir "))
for i in range (numeroveces):
    nota= float(input("Introduce la nota : "))
    if nota <0:
        negativos=negativos+1
    elif nota>0:
        positivos=positivos+1
    else:
        ceros=ceros+1
        print(f"hay {positivos} numero/s positivo/s")
        print(f"hay {ceros} cero/s")
        print(f"hay {negativos} numero/s negativo/s")


