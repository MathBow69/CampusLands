from math import sqrt

area = 0

print ("Ingrese la medida de uno de los lados del triángulo")
lado = int(input("-->   "))

aux1 = lado/2
aux2 = (lado*lado)-(aux1*aux1)
area = (lado*sqrt(aux2))/2

if area>1000:
    print("<DATOS NO VÁLIDOS=")

else:
    print("El área es:  ",area)