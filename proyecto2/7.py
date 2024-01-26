
cargo  = str(input("Ingrese su cargo, Planta o Administrativo: P/A    ")).upper()
horas  =int(0)
horas = int(input("Ingrese las horas trabajadas:  "))

if cargo == "P":
    print("Su pago es:  ",(horas*20000))
if cargo == "A":
    print("Su pago es:  ",(horas*10000))
else:
    print("Intente de nuevo ")