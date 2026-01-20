
listaletras=[]
listaletras2=[]
letra=input("introduce una letra ")
listaletras.append(letra)
#print(listaletras)
seguir=input("quieres introducir otre letra? si/no: ")
if seguir== "si":
    letra=input("introduce una letra ")
    listaletras.append(letra)
    seguir=input("quieres introducir otre letra? si/no: ")
elif seguir== "no":
    listaletras2=list(set(listaletras))
    print(listaletras2)
 