

lista = ['a','b','D','x','r','X','3','h','w','2','i'] 
while True: 
    valor = input("Introduce el valor que deseas eliminar: ") 
    if valor.isdigit(): 
        if valor in lista: 
            lista.remove(valor) 
            print(lista) 
        else: 
           print("El valor introducido no está en la lista") 
    else: 
        print("Introduce valor numérico") 
    if input("Deseas introducir otro valor s/n: ").lower() == "n": 
        break 