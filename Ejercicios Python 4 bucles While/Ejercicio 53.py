

si=1
no=1
var1=1
repe=0
while var1==1:
    num1=float(input("introduce un primer numero "))
    num2=float(input("introduce un segundo numero "))
    total=num1+num2
    print(f"la suma de los 2 digitos es {total}")
    rep=input("quieres volver a hacerlo (si/no) ")
    if rep=="si":
        var1=1
        repe=repe+1
    elif rep == "no":
        var1=3
    total2=total+total
print(f"la suma de todos los numeros es {total2}, y las repeticiones son {repe}")
