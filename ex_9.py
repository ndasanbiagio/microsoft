def invertir_palabra(palabra):
    palabra_invertida = palabra[::-1].upper()
    return palabra_invertida


palabra = "Python"  

palabra_invertida_resultante = invertir_palabra(palabra)

print(f"Palabra original: {palabra}")
print(f"Palabra invertida: {palabra_invertida_resultante}")



#Otro ejercicio

def chequear_3_cifras(lista):
    lista_3_cifras = []
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        
        else:
            pass
    
    return lista_3_cifras

resultado = chequear_3_cifras([55,99,600])
print(resultado)