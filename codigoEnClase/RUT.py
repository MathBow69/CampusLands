cedula = int(input("Ingrese su cédula:\n--> ").__reversed__)
print(cedula)
multi=2
class numero:
    def __init__(self, name):
        self.name = name

    def __reversed__(self):
        return self.name[::-1]



cedula = numero(cedula)
print(reversed(cedula))
cedula== (reversed(cedula))

# for contador in range (len(cedula)):
#     if multi ==7:
#         multi ==2
#     cedula[contador]
#     pass
#     pass