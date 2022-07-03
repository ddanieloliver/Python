#count() conta quantas vezes o elemento que você deseja aparece no string
#replace( , ) troca um determinado elemento por outro dentro do string.
#strip() remove espaços em branco no inicio e no final da frase, assim como rstrip() remove apenas os espaços da direita, lstrip() esquerda
#split() quebra todas as palavrtas de uma frase, tranforma a frase em uma lista e redimenciona os indices, cada palavra terá um indice de 0 ao ::
#join() faz o contrario do split, ele junta tudo em uma só frase.
#slice - literalmente fateia um string de maneira que posso usar um slice com a segunite estrutura String[:::], o primeiro é inicio, o segundo é fim e o terceiro é o passo
'''5) Escreva uma função repeteVogal(s) que retorna a string s, mas com as vogais repetidas. Ex:
repeteVogais("Universidade") -> "UUniiveersiidaadee"
'''
def indentificaVogal(letra):
    vogais = 'aeiouAEIOU'
    if letra in vogais:
        return True
    else:
        return False

def repeteVogais(s):
    string = ""
    for i in s:
        if indentificaVogal(i):
            string += i*2
        else:
            string += i
    print(string)
repeteVogais("Universidade")