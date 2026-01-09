#Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida

I1= int(input("Introduce el primer número: ")) 
I2 = int(input("Introduce el segundo número: ")) 
if I1<I2: 
    for j in range(I1,I2+1): 
        print(j, end="-") 
else: 
    for j in range(I1,I2 -1,-1): 
        print(j, end="-") 
    