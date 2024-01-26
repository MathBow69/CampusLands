voltajeActual =0

for contador in range(1,6,1):
    print ("ingrese el",contador, "voltaje a promediar")
    voltajeIngresado= int(input("-->    "))
    voltajeActual = voltajeIngresado+voltajeActual

if voltajeActual/5>220:
    print("<ALTO VOLTAJE=")
    
else:
    print("<VOLTAJE CORRECTO=")