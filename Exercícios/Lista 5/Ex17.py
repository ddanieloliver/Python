'''17) Escreva uma função divideNumeros(l,p) que retorna a tupla (menores,maiores), onde
menores é uma lista contendo todos os elementos da lista l menores do que p e maiores é uma
lista contendo todos os elementos da lista l maiores ou iguais a p.'''
lista = [1,2,3,4,5,6,8,7,9,14,45,21,47,123,54,19]
numero = int(input("Insira o numero: "))
def divideNumeros(l,p):
    menores = []
    maiores = []
    for i in l:
        if i < p:
            menores.append(i)
        if i > p:
            maiores.append(i)
    tupla = (menores, maiores)
    return tupla
print(divideNumeros(lista,numero))
