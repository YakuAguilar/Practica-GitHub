milista=[1,2,3,4,5,6]
milistapor2=[]
maximo=max(milista)
minimo=min(milista)
suma=sum(milista)
print(milista)
print("maximo:",maximo)
print("minimo:",minimo)
print("suma total:",suma)


for x in range (len(milista)):
    calculo=milista[x]*2
    milistapor2.append(calculo)

for x in milista:
    milistapor2.append(x*2)

milistapro=[n*2 for n in milista]
print(milistapro)


