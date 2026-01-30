numinicio=[]
letrasDNI=["T, R, W, A, G, M, Y, F, P, D, X, B, N, J, Z, S, Q, V, H, L, C, K, E"]
numinicio=int(input("introduce un numero de 8 digitos "))
for x in range(len(numinicio)):
    if len==8:
        resto=numinicio%23
    if resto==0:
        print(f"{numinicio*23}-,T")
    elif resto==1:
        print(f"{numinicio*23}-,R")
    elif resto==2:
        print(f"{numinicio*23}-,W")
    elif resto==3:
        print(f"{numinicio*23}-,A")
    elif resto==4:
        print(f"{numinicio*23}-,G")
    elif resto==5:
        print(f"{numinicio*23}-,M")
    elif resto==6:
        print(f"{numinicio*23}-,Y")
    elif resto==7:
        print(f"{numinicio*23}-,F")
    elif resto==8:
        print(f"{numinicio*23}-,P")
    elif resto==9:
        print(f"{numinicio*23}-,D")
    elif resto==10:
        print(f"{numinicio*23}-,X")
    elif resto==11:
        print(f"{numinicio*23}-,B")
    elif resto==12:
        print(f"{numinicio*23}-,N")
    elif resto==13:
        print(f"{numinicio*23}-,J")
    elif resto==14:
        print(f"{numinicio*23}-,Z")
    elif resto==15:
        print(f"{numinicio*23}-,S")
    elif resto==16:
        print(f"{numinicio*23}-,Q")
    elif resto==17:
        print(f"{numinicio*23}-,V")
    elif resto==18:
        print(f"{numinicio*23}-,H")
    elif resto==19:
        print(f"{numinicio*23}-,L")
    elif resto==20:
        print(f"{numinicio*23}-,C")
    elif resto==21:
        print(f"{numinicio*23}-,K")
    elif resto==22:
        print(f"{numinicio*23}-,E")