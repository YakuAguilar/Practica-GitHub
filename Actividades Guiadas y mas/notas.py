#Operador	Descripción	Uso
#+	Realiza Adición entre los operandos	12 + 3 = 15
#-	Realiza Substracción entre los operandos	12 - 3 = 9
#*	Realiza Multiplicación entre los operandos	12 * 3 = 36
#/	Realiza División entre los operandos	12 / 3 = 4
#%	Realiza un módulo entre los operandos	16 % 3 = 1
#**	Realiza la potencia de los operandos	12 ** 3 = 1728
#//	Realiza la división con resultado de número entero	18 // 5 = 3
print("       menu    ")
print("1. hamburguesa")
print("2. pizza")
print("3. lentejas")
print("4. bocadillo de jamon")

opcion=int(input("intoduce el numero del menu "))

if opcion==1:
    print("has escogido hamburguesa")
if opcion==2:
    print("has escogido pizza")
if opcion==3:
    print("has ecogido lentejas")
if opcion==4:
    print("has escogido bocadillo de jamon ")