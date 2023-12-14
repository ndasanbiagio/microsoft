def todos_positivos(lista):
    """
    Verifica si todos los valores en la lista son positivos.

    Parameters:
    - lista: Una lista de números.

    Returns:
    - True si todos los valores son positivos, False si al menos uno es negativo.
    """
    return all(x > 0 for x in lista)

# Lista de ejemplo con valores positivos y negativos
lista_numeros = [3, 7, -2, 10, 5]

# Verificar si todos los valores en la lista son positivos
resultado = todos_positivos(lista_numeros)

# Imprimir el resultado
print(resultado)


#Ejercicio

def suma_menores(lista):
    # """
    # Suma los números mayores a 0 y menores a 1000 en la lista.

    # Parameters:
    # - lista: Una lista de números.

    # Returns:
    # - La suma de los números que cumplen con las condiciones.
    # """
    return sum(x for x in lista if 0 < x < 1000)

# Lista de ejemplo con valores positivos y negativos
lista_numeros = [3, 7, -2, 10, 5, 500, 800, 1200]

# Calcular la suma de los números mayores a 0 y menores a 1000
resultado_suma = suma_menores(lista_numeros)

# Imprimir el resultado
print(resultado_suma)
