#Ejercicio de eleccion de palitos

from random import shuffle

#Lista nicial
palitos = ['-', '--', '---', '----']


#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista



#Pedir intentos
def probar_suerte():
    intento = ''
    
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4: ')
        
    return int(intento)
        

# Comprobar intentos

def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Perdiste")
        
    else:
        print("Te salvaste")
        
    print(f"Te ha tocado {lista[intento-1]}")
    
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)