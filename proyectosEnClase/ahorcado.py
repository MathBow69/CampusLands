palabra ="Hola Mundo".upper()
total = len (palabra)
intento = 3
for i,item in enumerate(palabra):
    letra = input ("Ingrese letra :").upper()
    if (letra in item):
        total -=1
        palabra = palabra.replace(letra,"-")
        if total == 0:
            print("gano")
            break
    else:
        intento -=1
    if intento == 0:
        print ("Perdiste")
        break