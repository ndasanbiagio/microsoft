from collections import Counter
from collections import defaultdict #Diccionario por defecto
from collections import namedtuple

serie = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,6])
print(serie.most_common())

print(list(serie))


#Ejercicio con defaultdict
mi_dic = {'uno':'verde', 'dos':'azul','tres':'rojo'}

print(mi_dic['dos'])



dic = defaultdict(lambda: 'nada')
dic['cinco'] = 'negro'

print(dic['uno'])

print(dic)


# Ejercicio namedtuple - imprimo lo que necesito de la tupla por su nombre

Persona = namedtuple('Persona',['nombre','altura','peso'])
nico = Persona('Nico', 1.75, 92)

print(nico.altura)