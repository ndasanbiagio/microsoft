#Simple ejercicio

mi_archivo = open('Prueba.txt')

# print(mi_archivo.read())

una_linea = mi_archivo.readline()
print(una_linea.upper())

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)


for l in mi_archivo:
    print("Aqui dice: " + l)






mi_archivo.close




# #Otro ejercicio

mi_archivo = open('Prueba.txt')



primera_linea = mi_archivo.readline()
print(primera_linea)







mi_archivo.close




#Otro ejercicio
archivo = open('Prueba.txt', 'a')

archivo.write('Hola\n')
archivo.write('Mundo')

archivo.close



#Correcion


archivo = open('mi_archivo.txt', 'w')

archivo.write('Nuevo\n')
archivo.write('texto')

print(archivo)







archivo.close
