#Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra


palabra=(input("introduce una palabra "))
for i in range(len(palabra)):
    print(f"en la posicion {i} esta la letra {palabra[i]}")