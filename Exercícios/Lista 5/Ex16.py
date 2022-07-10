'''16) Escreva uma função ordenacaoSelecao(l) que reutiliza a função da questão anterior para
ordenar uma lista de números. Não é permitido utilizar funções como sort. Ex:
ordenacaoSelecao([10, 6, 7, 1, 2, 4, 11, 24]) [1, 2, 4, 6, 7, 10, 11, 24]'''



array = [10, 6, 7, 1, 2, 4, 11, 24]

def ordenacaoSelecao(l):
    lista = []
    
    while len(l) > 0:
        min = l[0]
        for i in l:
            if i < min:
                min = i       
        lista.append(min)
        l.remove(min)
    
    return lista
print(ordenacaoSelecao(array))