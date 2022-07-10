'''11) Escreva uma função limites(l) que recebe uma lista l de números e retorna uma tupla
(min,max), onde min representa o menor dos elementos da lista e max o maior dos elementos da
lista. Não utilize funções prontas para determinar o menor ou maior elemento da lista.
'''

def limites(l):
    min = l[0]
    max = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
        if l[i] > max:
            max = l[i]
    final = (min, max)
    print(final)

l = [1, 7, 8, 9]
limites(l)