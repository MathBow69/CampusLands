from tabulate import tabulate

table = [["Sun"],["Earth"],["Moon"],["Mars"]]


print(tabulate(table, headers=["Planet"],tablefmt="rounded_grid",numalign="center"))
opciones =[["1. Añadir equipo"],["2. Jugar partido"],["3. Resultados"],["4. Salir"]]