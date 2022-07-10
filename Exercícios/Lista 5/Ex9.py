'''9) Crie uma função numerosAleatorios(n, min, max) que retorna uma lista com n números
inteiros entre os valores min (incluso) e max (não incluso). Ex:
numerosAleatorios(5,10,30) [13,29,23,13,21]'''

import random


def numerosAleatorios(n, min, max):
    lista = [min]
    for i in range(n-1):    
        x = random.randint(min,max-1)
        lista.append(x)
    return lista
print(numerosAleatorios(5,10,30))
