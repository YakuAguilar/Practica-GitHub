

I1= int(input("Introduce el primer número: ")) 
I2 = int(input("Introduce el segundo número: ")) 
if I1<I2: 
    for j in range(I1,I2+1): 
        print(j, end="-") 
else: 
    for j in range(I1,I2 -1,-1): 
        print(j, end="-") 
    