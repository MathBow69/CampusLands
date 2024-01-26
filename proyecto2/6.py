factura = 0
while True :
    bebida = int(input("Ingrese el valor de la bebida:  "))
    factura = factura+bebida
    fig  = str(input("¿Desea comprar otra bebida? S/N  ")).upper()
    if factura>130000:
        factura = factura -(factura*0.15) 
    if fig == "N":
        print("El valor de su compra es:    ",factura)
        break
