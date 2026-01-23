

import random 
lista = ["casa","barco","gato","perro","madera","agua","puente","pantalón"] 
secreta = random.choice(lista) 
intentos = 0 
while True: 
    intentos += 1 
    palabra = input("Introduce la palabra secreta: ") 
    if palabra == secreta: 
        print("ACERTASTE")
 
        break 
    else:
        print("SIGUE JUGANDO") 
