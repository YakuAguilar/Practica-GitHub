
si=()
no=()
listaletras=[]
seguir=()

letra=input("introduce una letra entre comillas ")
listaletras.append(letra)
#print(listaletras)
seguir=input("quieres introducir otre letra? si/no: ")
if seguir== si:
    letra=input("introduce una letra entre comillas ")
    listaletras.append(letra)
elif seguir== no:
    print(listaletras)

