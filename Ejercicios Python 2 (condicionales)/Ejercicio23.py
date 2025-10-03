#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos
var1=int(input("introduce tu nota "))
if var1<0 or var1>10:
    print("la nota es mayor de 10 o menor de 0")
elif var1<5:
    print("has sacado un insuficiente")
elif var1>=5 and var1<=6.5:
    print("has sacado un satisfactorio")
elif var1>=6.5 and var1<8.5:
    print("has sacado un notable")
elif var1<=10 and var1>8.5:
    print("has sacado un excelente")