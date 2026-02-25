import random
lista_palabrasecretas=["Patata", "Perro", "Ordenador", "Teclado", "Estuche", "Raton", "Movil", "Mochila", "Zapatos", "Rascacielos"]
# Palabra seleccionada aleatoriamente de la lista secreta
palabra_secreta = random.choice(lista_palabrasecretas)
# Lista de partida inicia con guiones según la longitud de la palabra secreta
Lista_partida = ["_" for _ in palabra_secreta]
# Lista de errores para el ahorcado
Lista_ahorcado = []
# Letras que representan el ahorcado
letras_ahorcado = list("AHORCADO")
# Contador de errores
errores = 0
# Función para mostrar el estado actual de la partida
def mostrar_estado():
    print("Palabra: " + " ".join(Lista_partida))
    print("Errores: " + " ".join(Lista_ahorcado))
# Función principal del juego
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
# Ejecutar el juego
if __name__ == "__main__":
    jugar_ahorcado()

