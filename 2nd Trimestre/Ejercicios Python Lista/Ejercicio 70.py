
milista2=[]
milista=[]
longitud=int(input("introduce la longitud de la lista "))

for x in range (0,longitud):
    numero=int(input("introduce un valor "))
    milista.append(numero)
    milista2=milista.copy()
    milista2.reverse()
print(milista2)