# Python
# Juego del Ahorcado mejorado con flujo completo después de `while True`

import random

# Lista de palabras
Lista_palabrasecreta = ["python", "programa", "juego", "computadora", "raton", "teclado", "monitor", "laptop", "codigo", "pantalla"]
palabra_secreta = random.choice(Lista_palabrasecreta)  # Elegir palabra al azar
Lista_partida = ["_"] * len(palabra_secreta)           # Guiones bajos para mostrar aciertos
Lista_ahorcado = ["A", "H", "O", "R", "C", "A", "D", "O"]  # Letras del ahorcado
errores = 0
letras_adivinadas = []  # Para evitar repetir letras

print("Bienvenido al juego del Ahorcado")
print("Intenta adivinar la palabra secreta")

while True:
    print("
Palabra a adivinar: ", " ".join(Lista_partida))
    letra = input("Introduce una letra: ").lower()

    if letra in letras_adivinadas:
        print("Ya has introducido esa letra. Prueba otra.")
        continue
    letras_adivinadas.append(letra)

    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                Lista_partida[i] = letra
        print("¡Bien! Has acertado una letra.")
    else:
        print("Letra incorrecta.")
        errores += 1
        if errores <= len(Lista_ahorcado):
            print("Ahorcado:", " ".join(Lista_ahorcado[:errores]))

    # Condición de victoria
    if "_" not in Lista_partida:
        print("
¡Felicidades! Has adivinado la palabra:", palabra_secreta)
        break

    # Condición de derrota
    if errores >= len(Lista_ahorcado):
        print("
Has perdido. La palabra correcta era:", palabra_secreta)
        break

print("Gracias por jugar al Ahorcado")