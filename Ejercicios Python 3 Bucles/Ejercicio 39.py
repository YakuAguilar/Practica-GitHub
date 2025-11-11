
negativos=0
positivos=0
ceros=0
numeroveces=int(input("introduce el numero de notas que quieres introducir "))
for i in range (numeroveces):
    nota= float(input("Introduce la nota : "))
    if nota <0:
        negativos=negativos+1
        print(f"hay {negativos} numeros negativos")
    elif nota>0:
        positivo=positivo+1
        print(f"hay {positivos} numeros positivos")
    elif:
        ceros=ceros+1
        print(f"hay {ceros} ceros")


