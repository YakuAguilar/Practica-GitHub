

listanumeros=[]
listanonumeros=[]
listatodo=[]
frase=input("introduce valores separados por un guion ")
#.split=para separar los digitos con un signo
listatodo=frase.split("-")

for x in range(len(listatodo)):
    if listatodo[x].isnumeric():
        listanumeros.append(listanumeros[x])
    else:
        listanumeros.append(listatodo[x])
#append= añade unn valor al final de la lista
print(listanumeros)
print(sum(listanumeros))