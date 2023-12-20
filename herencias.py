# class Animal:
    
#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color
 
 
#     def nacer(self):
#         print("Este animal ha nacido")

# class Pajaro(Animal):
#     pass


# piolin = Pajaro(2, 'amarillo')

# # piolin.nacer()

# # print(Pajaro.__base__)




#NUevo

class Padre:
    def hablar(self):
        print("Hola")
        

class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print('que tal')


class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass



mi_nieto = Nieto()

# mi_nieto.reir()
mi_nieto.hablar()
print(Nieto.__mro__)