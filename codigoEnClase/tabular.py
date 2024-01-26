import os
#primero hay que abrir cmd como admin e instalar tabulate, escribiendo "pip install tabulate"
from tabulate import tabulate

os.system('clear')
equipos = [["A. Bucaramanga",0,0],["A. Nacional",0,0]]
print(tabulate(equipos,headers=["Equipo","PJ","PG"]))
