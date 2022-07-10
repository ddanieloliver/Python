'''10) Escreva uma função media(l) que recebe uma lista l de números e retorna a média dos valores
da lista. Não utilize funções prontas de somatório ou média dentro de sua função.
'''

l = [1,3,6,7,4,98,7,6,5,4,3,10,15,1000]

def media(lista):
    somatorio = 0
    divide = 0

    for i in lista:
        somatorio += i
        divide += 1
    media = somatorio/divide
    return media

print(f" A média é {media(l):,.2f}")