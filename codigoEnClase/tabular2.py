import os
from tabulate import tabulate
os.system('cls')
equipos = [['A',9],['B',2],['c',1],['d',0]] 
orden = equipos.sort()
for i,item in enumerate(equipos):
    for j in range(int(i+1),len(equipos),1):
        if(equipos[i][1] > equipos[j][1]):
            aux = equipos[i]
            equipos[i]= equipos[j]
            equipos[j] = aux
print(tabulate(equipos,headers=['Indice','Equipo','PJ','PG'],tablefmt="fancy_grid",showindex=True,numalign="center"))
print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],headers="firstrow"))

#  nombre del equipo
#  partidos jugados = PJ
# partidos ganados = PG
# partidos perdidos = PP
# partidos empatados = PE
# goles a favor = GF
# goles en contra =GC
# total de puntos =TP