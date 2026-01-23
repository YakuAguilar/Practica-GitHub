

lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]

repetidas=list(set(lista1) & set(lista2)) 
no_repetidas=[palabra for palabra in lista2 if palabra not in lista1] 
print("Están repetidas:", repetidas) 
print("No están repetidas:", no_repetidas) 