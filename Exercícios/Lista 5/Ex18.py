'''18) Escreva uma função combina(l1,l2) que recebe duas listas de números l1 e l2. Assuma que
ambas as listas já tenham seus valores ordenados. Agrupe os elementos de ambas as listas em uma
única lista, contendo todos os valores em ordem crescente, e retorne essa lista'''

lista1 = [4,6,8,10]
lista2 = [11,13,15,17]

lista3 = [1,1,5,1,8941,4,84,1,84,5,124,8,3,2,65,48]
lista4 = [11,2,51,89,4,18,45,198,45,19,845,198,498,49]

def combina(l1,l2):
    juntas = l1 + l2
    juntas = sorted(juntas)
    return juntas

print(combina(lista1, lista2))
print(combina(lista3, lista4))