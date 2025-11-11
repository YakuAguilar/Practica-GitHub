
# Pedimos al usuario la cantidad de notas a introducir
total_notas = int(input("¿Cuántas notas deseas introducir? "))
        
        # Usamos un bucle para iterar por la cantidad de notas
for i in range(1, total_notas + 1):
            # Solicitamos cada nota
    nota = float(input(f"Introduce la nota {i}: "))
            
            # Verificamos si la nota es válida (0-10)
if nota < 0 or nota > 10:
    print("Nota no válida, debe estar entre 0 y 10.")
    # Pasamos a la siguiente iteración
            
            # Determinamos aprobado o suspendido
if nota >= 5:
    print(f"Nota {i}: Aprobado")
else:
    print(f"Nota {i}: Suspendido")