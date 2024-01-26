import os
import time


os.system ('clear')
titulo = """
    ++++++++++++++++++++++++++++++
    +    OPERACIONES CON LISTAS  +
    ++++++++++++++++++++++++++++++  
"""

opciones = "1. Agregar camper\n2. Eliminar camper \n3. Buscar camper \n4. Salir"
isActivate = True
campers =[]
while isActivate:
    os.system('clear')
    print(titulo)
    print(opciones)
    op = int (input(":) "))

    if (op == 1):
        id = str (len(campers)).zfill(5)
        nombre = input ("ingrese Nombre del camper")
        campers.append([id,nombre])
    elif (op ==2):

          nombre = input ("ingrese Nombre a eliminar")
          for i,item in enumerate(campers):
            if (nombre in item):
              campers.pop(i)
              break
    elif (op ==3):
        nombre = input ("ingrese Nombre a buscar")
        for item in campers:
            if (nombre in item):
                print (f'codigo:{item[0]}')
                print (f'nombre:{item[1]}')
                time.sleep(10) 
    elif (op ==4):
        isActivate = False
        print ("grax por part")
        os.system('pause')
    else:
        os.system('clear')
        print("otra vez")
        os.system ('pause')

# 3. REPORTES
#     A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO
#     B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE
#     C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO
#     D. TOTAL DE GOLES ANOTADOS POR TODOS LOS EQUIPOS
#     E. PROMEDIO DE GOLES ANOTADOS EN EL TORN
        