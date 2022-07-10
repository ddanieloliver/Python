'''14) Escreva uma função slice(l,i,f) que recebe uma lista l e dois números inteiros i e f e
retorna a mesma coisa que l[i:f], mas sem usar as slices da linguagem Python.
'''
l = [12,6,45,7,81,27,16]
i = int(input("Insira o inicio do slice:"))
f = int(input("Insira o final do slice:"))

print(l[i:f])

def slice(lista,inicio,fim):
    novaLista = []
    for i in range(len(lista)):
        if i >= inicio and i < fim:
            novaLista.append(lista[i])        
    return novaLista

print(slice(l,i,f))