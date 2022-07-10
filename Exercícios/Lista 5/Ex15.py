'''15) Escreva uma função menorFrente(l) que recebe uma lista de números e retorna a mesma lista
com a seguinte alteração: o menor número da lista está posicionado na primeira posição. Ex:
menorFrente([10, 6, 7, 1, 2, 4, 11, 24]) [ → 1, 10, 6, 7, 2, 4, 11, 24]'''

def menorFrente(lista):
    menor = lista[0]
    contadorIndice = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            contadorIndice = i
    del lista[contadorIndice]
    lista[0:0] = [menor]
    return lista

l = [10, 6, 7, 1, 2, 4, 11, 24]
print(menorFrente(l))