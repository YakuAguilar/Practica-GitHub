#num<0
negativos=0
positivos=0
x=0
for x in range (6):
    var1=float(input("introduce un numero "))
    if var1<0:
        negativos=negativos+var1
    if var1>0: 
        positivos=positivos+var1
print(f"la suma total de los positivos es: {positivos}")
print(f"la suma total de los negativos es: {negativos}")
