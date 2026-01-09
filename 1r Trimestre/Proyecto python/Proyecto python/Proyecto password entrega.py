
print("                     Crea tu Password                       ")
print("El password tiene que tener mas de 6 y menos de 8 caracteres")
print("Posicion 1: Un numero major o igual a 1 o igual a 5         ")
print("Posicion 2: Una letra minuscula                             ")
print("Posicion 3: Una letra mayuscula                             ")
print("Posicion 4: Uno de los siguientes simbolos:*,_,@            ")
print("Posicion 5: Una letra minuscula                             ")
print("Posicion 6: Un numero major o igual a 6 y mneor o igual a 9 ")
print("Posicion 7: Uno de los siguinetes simbolos: &,/,#           ")
print("Posicion 8: Un numero menor o igual que 5                   ")
#fraseerrrores= fraserrores  +  erro?
#chivato=chivato + 1
correctos=0
incorrecto=0
Password=str(input("introduce un Password "))
print(Password[0])
if Password[0] >=1 or Password[0]==5:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1
print(Password[1])
if Password[1]:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1
print(Password[2])
if Password[2] >=1 or Password[2]==5:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1
print(Password[3])
if Password[3] >=1 or Password[3]==5:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1
print(Password[4])
if Password[4] >=1 or Password[4]==5:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1
print(Password[5])
if Password[5] >=1 or Password[5]==5:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1
print(Password[6])
if Password[6] >=1 or Password[6]==5:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1
print(Password[7])
if Password[7] >=1 or Password[7]==5:
    correctos=correctos+1
else:
    incorrecto=incorrecto+1

if incorrecto==0<1:
    print("la contraseña no cumple las instrucciones inicales")
else:
    print("la contraseña a sido creada con exito ")
#Longitudpassword=len(Password)




















