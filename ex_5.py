from random import randint
import random

aleatorio = randint(1,50)
print(aleatorio)




# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación,
# y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

aleatorio_new = random.choice(nombres)

print(aleatorio_new)




#Nuevo Ejercicio


palabra = "Don Nico"

lista = [letra for letra in palabra ]

print(lista)

newLista = [letra for letra in "Nico"]

print(newLista)



#Nuevo Ejercicio


lista1 = [n if n *2 > 10 else 'no' for n in range (0,21,2)]
print(lista1)



#Nuevo Ejercicio
#Pasar de pies a metro

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]

print(metros)


# Nuevo Ejercicio

def evaluar_valor(valor):
    match valor:
        case 1:
            print("El valor es 1")
        case 2:
            print("El valor es 2")
        case _:
            print("El valor no es ni 1 ni 2")

# Ejemplo de uso
evaluar_valor(1)
evaluar_valor(3)
