
import unicodedata

listaletras=[]
listaletras2=[]
while True:
    letra=input("introduce una letra ")
    if letra.isalpha() and letra is not listaletras:
        letra=unicodedata.normalize("NFD", letra)
        listaletras.append(letra)
        if input("quieres introducir otre letra? si/no: ").lower()== "no":
            break
listaletras2=list(set(listaletras))
print(listaletras2)
