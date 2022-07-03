'''3) Escreva uma função removePedaco(s,p) que recebe uma string s e remove todas as vezes em
que a string p aparece dentro de s. Ex:
removePedaco("Universidade Federal","idade") "Univers Federal"'''
#count() conta quantas vezes o elemento que você deseja aparece no string
#replace( , ) troca um determinado elemento por outro dentro do string.
#strip() remove espaços em branco no inicio e no final da frase, assim como rstrip() remove apenas os espaços da direita, lstrip() esquerda
#split() quebra todas as palavrtas de uma frase, tranforma a frase em uma lista e redimenciona os indices, cada palavra terá um indice de 0 ao ::
#join() faz o contrario do split, ele junta tudo em uma só frase.
#slice - literalmente fateia um string de maneira que posso usar um slice com a segunite estrutura String[:::], o primeiro é inicio, o segundo é fim e o terceiro é o passo

s = str(input('Insira seu string: '))
p = str(input('Insira o pedaço a ser removido: '))
def removePedaco(string, pedaco):
    stringSemPedaço = string.replace(pedaco, "")
    print(stringSemPedaço)
removePedaco(s, p)
