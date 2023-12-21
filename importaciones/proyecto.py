import re
import os
import time
import datetime
from pathlib import Path
import math


#Primero coloco las variables
inicio = time.time()

ruta = 'C:\\User\\Win10\\Desktop\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []


#Luego armo las funciones
def buscar_numeros(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else: 
        return ''
    

def crear_listas():
    for carpeta, subcarpetas, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numeros(Path(carpeta, a), mi_patron)
            if resultado != '':
                nros_encontrados.append((resultado.group()))
                archivos_encontrados.append(a.title())
                

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de Busuqeda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t-------')
    for a in archivos_encontrados:
        print(f'{a}\t{nros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros Encontrados: {len(nros_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)
    

crear_listas()
mostrar_todo()