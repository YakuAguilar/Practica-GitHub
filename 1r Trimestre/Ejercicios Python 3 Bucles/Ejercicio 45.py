#Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el stringdistinguiendo vocales y las consonantes:


palabra = input("Introduce una palabra: ") 
vocales = "" 
consonantes = "" 
for letra in palabra: 
    if letra in "aeiouáéíóú": 
        vocales += letra 
    else: 
        consonantes += letra 
print("Las vocales son:",vocales) 
print("Las consonantes son:",consonantes) 