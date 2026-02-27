import random
s=0
n=1
lista_palabrasecretas=["patata", "perro", "ordenador", "teclado", "estuche", "raton", "movil", "mochila", "zapatos", "rascacielos"]
palabra_secreta = random.choice(lista_palabrasecretas)
Lista_partida = ["_" for _ in palabra_secreta]
Lista_ahorcado = []
letras_ahorcado = list("AHORCADO")
errores = 0
def mostrar_estado():
    print("Palabra: " + " ".join(Lista_partida))
    print("Errores: " + " ".join(Lista_ahorcado))
def jugar_ahorcado():
    global errores
    print("¡Bienvenido al juego del Ahorcado!")
    while errores < 8 and "_" in Lista_partida:
        mostrar_estado()
        intento = input("Introduce una letra: ").lower()
        if len(intento) != 1 or not intento.isalpha():
            print("Introduce solo una letra válida.")
            continue
        if intento in palabra_secreta:
            for idx, letra in enumerate(palabra_secreta):
                if letra == intento:
                    Lista_partida[idx] = intento
            print(f"¡Bien! La letra '{intento}' está en la palabra.")
        else:
            if errores < 8:
                Lista_ahorcado.append(letras_ahorcado[errores])
                errores += 1
            print(f"¡Error! La letra '{intento}' no está en la palabra.")
    mostrar_estado()
    if "_" not in Lista_partida:
        print(f"¡Felicidades! Has adivinado la palabra: '{palabra_secreta}'")
    else:
        print(f"Has perdido. La palabra correcta era: '{palabra_secreta}'")
if __name__ == "__main__":
    jugar_ahorcado()
seguir_jugando=(input("¿deseas seguir jugando? s/n "))
if seguir_jugando==n:
    print("El juego se a acabado")
elif seguir_jugando==s:
    print("")

