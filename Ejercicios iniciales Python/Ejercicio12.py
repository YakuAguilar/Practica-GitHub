#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
var4=float(input("introduce los valores de lado "))
var1=float(input("introduce la base menor "))
var2=float(input("introduce la base mayor "))
var3=float(input("introduce la altura "))
print(f"el area del trapecio isósceles es {(var3*(var1+var2))/2}")
print(f"el perimetro del trapecio isósceles es {var1+var2+(var4*2)}")