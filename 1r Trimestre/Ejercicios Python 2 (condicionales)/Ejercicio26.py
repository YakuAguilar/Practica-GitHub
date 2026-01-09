#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.

var1=(input("introduce una letra "))

minuscula=False
mayuscula=False

if var1.isupper():
    mayuscula=True and print("la letra introducida es mayuscula")
elif var1.islower():
    minuscula=True and print("la letra introducida es minuscula")
else:
    print("esto no es una letra")
