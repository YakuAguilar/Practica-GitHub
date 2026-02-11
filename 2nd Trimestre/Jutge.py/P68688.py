
print("Hola a todos")


palabras=[]
for x in range (0,3):
    caractespalabra=(input("introduce 3 palabras, separadas por comas  "))
    palabras.append(caractespalabra)
    palabras2=palabras.copy()
    palabras2.reverse()
print(palabras2)