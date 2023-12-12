monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1

else:
    print("No tengo mas monedas")
    

#Otro ejercicio

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)



#Otro ejercicio

numeros = 10

while numeros >= 0:
    print(numeros)
    numeros -=1
 
 
#Otro ejercicio
 
numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero -= 1
    
    
    
#Otro ejercicio 
    
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')




#Ejercicio con ZIP

names = ["Nico", "Beni", "Ame", "Erika"]
age = [39, 8 , 5, 43]
city = ["Mendoza", "Cordoba", "Cordoba", "Rio de Janeiro"]

combination = list(zip(names, age, city))

for names,age,city in combination:
    print(f"{names} tiene {age} años y vive en {city}")
    
    
    
    
 #Ejercicio con ZIP   

# Crear el zip con las traducciones
traducciones = zip(['uno', 'dos', 'tres', 'cuatro', 'cinco'],
                   ['um', 'dois', 'três', 'quatro', 'cinco'],
                   ['one', 'two', 'three', 'four', 'five'])

# Convertir el zip a una lista
numeros = list(traducciones)

# Imprimir el resultado
print(numeros)



 #Ejercicio con min/max  

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

# Obtener el valor máximo
valor_maximo = max(lista_numeros)

# Imprimir el resultado o realizar cualquier otra operación con el valor máximo
print("El valor máximo en la lista es:", valor_maximo)
