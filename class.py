# class Personaje():
#     pass

# harry_potter = Personaje()
# print(harry_potter)


class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print('pio, mi color es {}'.format(self.color))
        
    
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")

piolin = Pajaro('amarillo', 'canario')
piolin.piar()

# mi_pajero = Pajaro('negro') 

# palabra = 'hola'

# print(mi_pajero.color)