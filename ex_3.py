lista = ["a", "b", "c", "d", "e"]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra} : {letra} ")
    

list = ["Nico" , "Beni", "Ame", "Erika"]

for nombre in list:
    if nombre.startswith("N"):
        print(nombre)
        
    else:
        print("""Nombre no empieza con "N" """)
        
        
palabra = "Python es Super!!! "

for letter in palabra:
    print(letter)
    
    

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = sum(lista_numeros)

print(suma_numeros)
