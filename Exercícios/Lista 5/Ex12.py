'''12) Escreva uma função contaPares(l) que recebe lista l de números inteiros e retorna a
quantidade de números pares presente na lista.'''
l = [1,26,2,24,6,5,4,7]
def contarPares(lista):
    contadorDePares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            contadorDePares += 1
    return contadorDePares

print(contarPares(l))