

letras = "TRWAGMYFPDXBNJZSQVHLCKE"
LISTA_INTENTOS=[]
continuar = "s"
while continuar.lower()=="s":
    dni= input("Introduce el número del DNI (8 dígitos): ")
    if len(dni) != 8:
        print("ERROR")
        LISTA_INTENTOS.append(0)
    elif not dni.isdigit():
        print("1")
        LISTA_INTENTOS.append(1)
    else:
        numero = int(dni)
        resto = numero % 23
        if 0 <= resto <= 22:
            letra = letras[resto]
            print(f"3 → DNI correcto: {dni}-{letra}")
            LISTA_INTENTOS.append(3)
        else:
            print("2")
            LISTA_INTENTOS.append(2)
    continuar = input("¿Deseas continuar? (s/n): ")
print("LISTA_INTENTOS:", LISTA_INTENTOS)