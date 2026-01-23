

lista = ['a','b','D','x','r','X','3','h','w','2','i'] 

numeros = [int(x) for x in lista if x.isdigit()]
letras = [x for x in lista if x.isalpha()] 
mayus = [x for x in letras if x.isupper()] 
print("Número de valores:", len(lista)) 
print("Cantidad de números:", len(numeros)) 
print("Cantidad de letras:", len(letras)) 
print("Cantidad de mayúsculas:", len(mayus)) 
print("Suma total de números:", sum(numeros)) 