voltajeActual =0


for contador in range(1,4,1):
    print ("ingrese el",contador, "voltaje a promediar")
    voltajeIngresado= int(input("-->    "))
    voltajeActual = voltajeIngresado+voltajeActual

if voltajeActual/3>220:
    print("<PELIGRO=")
    
elif voltajeActual/3>115 and voltajeActual/3 < 220:
    print("<ALTO VOLTAJE=")   

elif voltajeActual/3 < 115:
    print("<VOLTAJE CORRECTO=")