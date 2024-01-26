
import os
import time
from tabulate import tabulate
import array as arr



lista = ([8,"piruja",2,4,6],[9,"zorra",3,5,7])
lista[1][3] +=3
print (lista)
pendejo=lista[0][2]+52
lista[0][2:5] = arr.array("i",[10,pendejo,10])
print (lista[0])
