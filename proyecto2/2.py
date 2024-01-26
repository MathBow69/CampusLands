numero1 = int(input("Ingrese el primer número:"))
numero2 = int(input("Ingrese el segundo número:"))
if numero1>numero2:
    numero3 = int(input("Ingrese el tercer número:"))
    if numero1>numero3:
        print (f"El número mayor es {numero1}")
    else:
        print (f"El número mayor es {numero3}")
else:
    numero3 = int(input("Ingrese el tercer número:"))
    if numero2>numero3:
        print (f"El número mayor es {numero2}")
    else:
        print (f"El número mayor es {numero3}")
 
