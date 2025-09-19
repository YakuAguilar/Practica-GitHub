#. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
var1=float(input("introduce catidad de segundos "))
var2=60
var3=3600
totalminutos=var1/var2
totalhoras=var1/var3
print(f"{var1} son {totalminutos} minutos y {totalhoras} segundos")