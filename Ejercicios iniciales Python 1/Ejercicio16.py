#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división)
import math
var1=float(input("introduce un numero"))
raizcuadrada=round(math.sqrt(var1), 1)
print(f"la raiz cuadrada es {raizcuadrada}")
print(f" el resultado de la division es {raizcuadrada}")
