
numinicio=[]
letrasDNI=["T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E"]
numinicio=(input("introduce un numero de 8 digitos "))
for x in range (len(str(numinicio))):
    if (len(str(numinicio))) ==8:
        resto=numinicio%23
        if resto==0:
            print()


dni_numero=(input("introduce un numero de 8 digitos "))
tabla_letras="TRWAGMYFPDXBNJZSQVHLCKE"
resto = dni_numero % 23
return tabla_letras-[resto]


