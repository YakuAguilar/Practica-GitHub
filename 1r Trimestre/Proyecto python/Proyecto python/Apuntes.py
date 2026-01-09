#str=para los metodos string

#for:bucle dpara repetir palabras
#for j in range (0,10): #de 0 a 10
#for j in range (0,10,2): #de 0 a 10 con intervalos de 2
#otra manera(for j in string)
#while: bucle con condicion dentro donde cuando se cumpla se parara(puede depender del usuario las veces quer se repita)

total=0
#repeticiones=int(input("numero de veces ")
#for j in range (repeticiones):
 #   print(j,"hola")
   #total=total+j
#print(total)


password="a7e4jkE"
vocales="aeiouAEIOU"
TOTAL=0
for i in password:
    if i.isnumeric():
        TOTAL=TOTAL + int(i)
print(TOTAL)
#suma total de los muneros y numero de vocales