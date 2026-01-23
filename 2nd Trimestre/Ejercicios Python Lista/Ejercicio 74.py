
lista1 = ["casa","mesa","sal","sol","agua"] 
lista2 = ["casa","luz","tres","tren","sol","pan"] 
repetidas = list(set(lista1) & set(lista2)) 
no_repetidas = list(set(lista1) ^ set(lista2)) 
print("Están repetidas:", repetidas) 
print("No están repetidas:", no_repetidas) 