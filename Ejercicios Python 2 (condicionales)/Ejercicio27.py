# Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla

var1=(input("introduce una letra "))

minuscula= False
mayuscula=False
numero=False

if var1.isupper():
    mayuscula=True and print("la letra introducida es mayuscula")
elif var1.islower():
    minuscula=True and print("la letra introducida es minuscula")
elif var1.isnumeric():
    munero=True and print("lo que has introducido es una numero")
else:
    print("¿la letra es mayuscula?")