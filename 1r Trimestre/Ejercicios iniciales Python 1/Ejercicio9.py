#programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
var1=float(input("introduce catidad de segundos "))
totalminutos=var1/60
totalhoras=var1/3600
print(f"{var1} son {totalminutos} minutos y {totalhoras} segundos")