fig  = str(input("Ingrese el tipo de figura el cual se calculará el área, para un Triangulo escriba T y para un Circulo escriba C:   ")).upper()
base = 0
altura = 0
radio = 0
pi = 3.1416


if fig =="T":
    base = int(input("Por favor ingrese la base del tríangulo:  "))
    altura= int(input("Ahora, por favor ingrese la altura del tríangulo:  "))
    print ("El valor del area es ", (base * altura)/2) 


elif fig =="C":
    radio = int(input("Por favor ingrese el radio del circulo:  "))
    print (f"El valor del area es ",(radio*radio*pi))
   
else:
    print ("No seleccionaste la figura adecuada, vuelve a iniciar el programa")

