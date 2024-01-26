
equipoA = str(input("Ingrese el nombre del primer equipo:   " ))
cA = int(input("Ahora ingrese sus canastas:    "))
equipoB = str(input("Ingrese el nombre del segundo equipo:"))
cB = int(input("Ahora ingrese sus canastas:    "))
if cA>cB:
    print ("El ganador fue",equipoA,", el perderor fue ",equipoB,"y la diferencia de canastas fueron:   ",(cA-cB) )
else:
    print ("El ganador fue",equipoB,", el perderor fue ",equipoA,"y la diferencia de canastas fueron:   ",(cB-cA) )