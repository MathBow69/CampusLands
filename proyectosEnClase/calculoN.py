condi = True
numero = int(0)
par = int(0)
impar = int(0)
prom = int(0)
cprom = int(1)
sum = int(0)
m50 = int(0)
m10 = int(0)
m0 = int(0)
while condi == True:
   
   input('Ingrese el número: ')
   if input==int:
    numero=input0
     (numero <0):
        print ("El numero de pares es:  ",par)
        print ("El numero de impares es:  ",impar)
        print ("El promedio es:  ",prom/cprom)
        print ("La sumatoria es:  ",sum)
        print ("El numero de mayores que 50 es:  ",m50)
        print ("El numero de mayores que 10 pero que menores de 50 es:  ",m10)
        print ("El numero de menores que 10 es:  ",m0)

        condi == False
    prom=prom+numero
    cprom+=1
    sum=sum+numero

    if (numero%2==0):
        par +=1
    else:
        impar +=1
    if (numero>50):
        m50 +=1
    elif (numero>10):
        m10 +=1
    else:
        m0 +=1
    

    

