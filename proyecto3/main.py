
import os
import time
from tabulate import tabulate
import array as arr

os.system ('cls')

for i in range(0, 101):
        os.system ('cls')
        print("Cargando ",i," % .....")
        time.sleep(0.005)

titulo = ["LIGA BETPLAY"]
opciones =[["1. Añadir equipo"],["2. Jugar partido"],["3. Resultados"],["4. Salir"]]

opciones2 = [["1. Equipo que mas goles anoto"],["2. Nombre del equipo que mas puntos tiene"],["3. Nombre del equipo que mas partidos gano"],["4. Total de goles anotados por todos los equipos"],["5. Promedio de goles anotados en el torne0"],["6. Salir"]]
liga =[]
isActive = True

while isActive:

    os.system('cls')

    print(tabulate(opciones,headers=titulo,tablefmt="rounded_grid",numalign="center",))
    op = int (input("Escoja su opción --> "))   

    if (op == 1):

        os.system('cls')
        temp = True
        
        while temp:
            os.system('cls')
            nombre = input ("ingrese el nombre del equipo\n--> ")
            liga.append([nombre,0,0,0,0,0,0,0])
            print("Desea añadir otro equipo?\n1) Si\n2) No\n")
            op = int (input("--> "))
            if (op == 2):
                temp = False

    elif (op == 2):
        print(tabulate(liga,headers=["Indice","Nombre del equipo","PJ","PG","PP","PE","GF","GC","TP"],tablefmt="fancy_grid",showindex=True,numalign="center"))
        
        local = int(input("Escoja del equipo local --> "))
        visitante = int(input("Escoja el equipo visitante -->  "))

        liga[local][1] +=1  
        liga[visitante][1] +=1
               
        gol1  = int(input("Ingrese los goles del equipo local -->  "))  
        gol2  = int(input("Ingrese los goles del equipo visitante -->  "))

        liga[local][5] +=gol1
        liga[visitante][5] +=gol2
        liga[local][6] +=gol2
        liga[visitante][6] +=gol1

        if (gol1 > gol2):
            liga[local][2] +=1
            liga[visitante][3] +=1
            liga[local][7] +=1
            
        elif gol1 < gol2:
            liga[visitante][2] +=1
            liga[local][3] +=1
            liga[visitante][7] +=3

        elif (gol1 == gol2):
            liga[local][4] +=1
            liga[visitante][4] +=1
            liga[local][7] +=1
            liga[visitante][7] +=1

    elif (op == 3):

        os.system('cls')
        temp = True

        while temp:

            print(tabulate(liga,headers=["Indice","Nombre del equipo","PJ","PG","PP","PE","GF","GC","TP"],tablefmt="fancy_grid",showindex=True,numalign="center"))
            print(tabulate(opciones2,headers=titulo,tablefmt="outline",numalign="center",))
            op = int (input("Escoja su estadística a buscar --> "))

            print ("Cargando su opción...")
            time.sleep(1)

            if (op == 1):
                os.system('cls')
                mejorEquipo=0
                for equipito in (range(0,len(liga))):
                    if liga[equipito][5] > liga[equipito-1][5]:
                        mejorEquipo=liga[equipito][0]
                print("El equipo goleador fue: ",mejorEquipo)
                input("Presione Enter para continuar ... ")

            elif (op == 2):
                os.system('cls')
                for equipito in (range(0,len(liga))):
                    if liga[equipito][7] > liga[equipito-1][7]:
                        mejorEquipo=liga[equipito][0]
                print("El equipo en cabeza es: ",mejorEquipo)
                input("Presione Enter para continuar ... ")

            elif (op == 3):
                os.system('cls')
                for equipito in (range(0,len(liga))):

                    if liga[equipito][2] == liga[equipito-1][2]:
                        os.system('cls')
                        print("Nadie ha ganado ningún partido hasta la fecha")

                    if liga[equipito][2] > liga[equipito-1][2]:
                        mejorEquipo=liga[equipito][0]
                        print("El equipo que más partidos ha ganado es: ",mejorEquipo)
               
                input("Presione Enter para continuar ... ")
                
            elif (op == 4):
                os.system('cls')
                puntajeTotal = 0

                for equipito in (range(0,len(liga))):

                    puntajeTotal += liga[equipito][5]                   
                print("Total de goles anotados: ",puntajeTotal)
                input("Presione Enter para continuar ... ")
                
            elif (op == 5):
                os.system('cls')
                puntajeTotal = 0
                prom = 0
                for equipito in (range(0,len(liga))):
                    puntajeTotal += liga[equipito][5]
                    prom += liga[equipito][1]        
                print("Promedio de goles anotados: ",puntajeTotal/prom)
                input("Presione Enter para continuar ... ")
                
            elif (op == 6):
                os.system('cls')
                print("Saliendo del programa...")
                time.sleep(1)
                temp = False
            else:
                print("Por favor dijite una verdadera opción")
    elif (op == 4):
        os.system('cls')
        print("Saliendo del programa...")
        time.sleep(1)
        isActive = False
        
    else:
        print("Por favor dijite una verdadera opción")
   