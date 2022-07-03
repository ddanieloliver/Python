#count() conta quantas vezes o elemento que você deseja aparece no string
#replace( , ) troca um determinado elemento por outro dentro do string.
#strip() remove espaços em branco no inicio e no final da frase, assim como rstrip() remove apenas os espaços da direita, lstrip() esquerda
#split() quebra todas as palavrtas de uma frase, tranforma a frase em uma lista e redimenciona os indices, cada palavra terá um indice de 0 ao ::
#join() faz o contrario do split, ele junta tudo em uma só frase.
#slice - literalmente fateia um string de maneira que posso usar um slice com a segunite estrutura String[:::], o primeiro é inicio, o segundo é fim e o terceiro é o passo

'''4) Escreva uma função contaVogais(s) que retorna a quantidade de vogais presente na string s.
Ex:
contaVogais("Universidade") 6 '''

s = str(input("Insira o string: "))
def verificaVogais(letra):
    vogais = 'aeiou'
    if letra in vogais:
        return True
    else:
        return False
def contaVogais(string):
    string = string.lower()
    contador = 0
    for i in string:
        if verificaVogais(i) == True:
            contador +=1
    print (contador)
contaVogais(s)
