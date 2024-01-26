cargo  = str(input("Ingrese su cargo, Planta o Administrativo: P/A    ")).upper()
horas  =int(0)
try:
    horas = int(input("Ingrese las horas trabajadas:  "))
except:
    print("Ingrese sus horas porfavor")
if cargo == "P":
    print("Su pago es:  ",(horas*20000))
if cargo == "A":
    print("Su pago es:  ",(horas*10000))
else:
    print("Intente de nuevo ")