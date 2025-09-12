#print es para que diga algo(primer ejemplo)
print ("Hello")
#print+(resultado de una variable)/("para que diga palabras literales")

# variable numerica
var1=4
# variable decimal
var2=4.5
#variable texto
var3="hola"
var4=6
total= var1 + var4
print ("la suma de ",var1," + ",var4,":",var1+var4)
#la f es otro formato de que el progama identifique la variable y la muestre
print (f"la suma de {var1} + {var4}: ",var1+var4 )
#se puede poner var1 + var4 o creamos otra variable que represente el total y colocamos esa variable.
print ("el kilo de tomates cuestan",total," de euros")
print ("el kilo de tomates cuestan",var1+var4," de euros")
#var1=input ("texto")
#int es para que lo asigne como numero entero y no como una cadena de texto
var5=int(input("introduce un numero "))
var6=int(input("introduce otro numero "))
total= var5+var6
print (" el resultado es ",total)
#float es para que lo asigne como numero decimal y entero 
var7=float(input("introduce un numero "))
var8=float(input("introduce otro numero "))
total= var7+var8
print (" el resultado es ",total)
