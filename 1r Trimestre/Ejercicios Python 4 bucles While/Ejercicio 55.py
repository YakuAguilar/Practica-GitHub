#Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While



si=1
no=1
var1=1
while var1==1:
    num1=float(input("introduce un primer numero "))
    num2=float(input("introduce un segundo numero "))
    total=num1+num2
    print(f"la suma de los 2 digitos es {total}")
    rep=input("quieres volver a hacerlo (si/no) ")
    if rep=="si":
        var1=1
    elif rep == "no":
        var1=3