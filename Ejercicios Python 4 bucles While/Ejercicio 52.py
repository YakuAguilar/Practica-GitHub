
si=1
no=1
#num1=float(input("introduce un primer numero "))
#num2=float(input("introduce un segundo numero "))
#total=num1+num2
var1=1
num1=float(input("introduce un primer numero "))
num2=float(input("introduce un segundo numero "))
while var1==1:
    total=num1+num2
    print(f"la suma de los 2 digitos es {total}")
    rep=input("quieres volver a hacerlo (si/no) ")
    if rep==si:
        num1=float(input("introduce un primer numero "))
        num2=float(input("introduce un segundo numero "))
    elif rep == no:
        print("programa finalizado")
        var1=3
        




        