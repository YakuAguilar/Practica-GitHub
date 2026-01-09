# Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While

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