base = 14400000

tiempo = int(input("Ingrese los años del trabajador:  "))

if tiempo>10:
    print("Tu sueldo ahora es:  	",base+(base*0.1))
elif tiempo>5:
    print("Tu sueldo ahora es:  	",base+(base*0.07))
elif tiempo>3:
    print("Tu sueldo ahora es:  	",base+(base*0.05))
else:
    print("Tu sueldo ahora es:  	",base+(base*0.03))
