'''13) Escreva uma função filtraPares(l) que recebe uma lista l de números inteiros e retorna uma
lista contendo apenas os números pares da lista entrada.'''

l = [1,26,2,24,6,5,4,7]
def filtraPares(lista):
    contadorDePares = []
    for i in lista:
        if i % 2 == 0:
            contadorDePares.append(i)
    return contadorDePares

print(filtraPares(l))