temperatura = int(input("Ingrese la temperatura:  "))
presion = int(input("Ingrese la presion:  "))

if temperatura>100 or presion >200 :
    print ("Alarma")
else:
    print ("Normal")