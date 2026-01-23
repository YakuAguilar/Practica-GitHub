

dato = input() 
try: 
    float(dato) 
    if "." in dato: 
        print("Es un número con decimales") 
    else: 
        print("No es un número con decimales") 
except: 
    print("No es un número con decimales") 