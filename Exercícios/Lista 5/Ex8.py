'''8) Escreva uma função busca(l, x) que procure o número x dentro da lista l e retorne um valor
booleano indicando se x está dentro da lista de números ou não. Não é permitido utilizar o operador
in nessa questão. Ex:
busca([2,4,6,8],4) True →
busca([2,4,6,8],3) False'''

l = [2,2,64,5,6]
x = int(input("Insira o numero:"))

def busca(lista, argumento):
     i= 0
     while i < len(l):
        if argumento== lista[i]:
           return True
        i= i+1
     return False    
print(busca(l,x))