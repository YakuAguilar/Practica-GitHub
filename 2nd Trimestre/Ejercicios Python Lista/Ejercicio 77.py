
lista = ['a','b','D','x','r','X','3','h','w','2','i'] 
letras = sorted([x for x in lista if x.isalpha()], key=str.lower) 
numeros = sorted([int(x) for x in lista if x.isdigit()]) 
op = int(input("Introduce 1 ascendente o 2 descendente: ")) 
if op == 2: 
    letras.reverse() 
    numeros.reverse() 
print(numeros) 
print(letras) 