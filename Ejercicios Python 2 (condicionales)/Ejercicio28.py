#Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
var1=(input("introduce una letra "))

minuscula= False
mayuscula=False
numero=False
simbolo=False

if var1.isupper():
    mayuscula=True and print("la letra introducida es mayuscula")
elif var1.islower():
    minuscula=True and print("la letra introducida es minuscula")
elif var1.isnumeric():
    munero=True and print("lo que has introducido es una numero")
elif var1.isalpha and not var1.isspace:
    simbolo=True and print=("el caracter introducido es un simbolo")
else:
    print("esto no es una letra")