

palabra = input("Introduce una palabra: ").lower()
vocales = "" 
consonantes = "" 
for letra in palabra: 
    if letra in "aeiouáéíóú": 
        vocales += letra 
    else: 
        consonantes += letra 
print("Las vocales son:", vocales) 
print("Las consonantes son:", consonantes) 