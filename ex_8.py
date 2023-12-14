
dic = {'clave1': 100, 'clave2': 500}

a = dic.popitem()
print(a)
print(dic)




#Ejercicio Nuevo


def potencia(base, exponente):
    resultado = base ** exponente
    return resultado
    
base = 2
exponente = 3

resultado_potencia = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado_potencia}")




#NUevo ejercicio

def usd_a_eur(monto_usd):
    tasa_conversion = 0.90
    monto_eur = monto_usd * tasa_conversion
    return monto_eur

dolares = 1000

monto_eur_resultante = usd_a_eur(dolares)

print(f"{dolares} USD equivalen a {monto_eur_resultante:.2f} EUR")
    