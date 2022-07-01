"""Crie uma função dobro(n) que recebe como parâmetro um número inteiro e devolve seu dobro."""

from random import triangular


def dobro(n):
    return 2*n
#print(dobro(2))

'''2) Crie uma função relogio_segundos(h,m,s) que receba três números inteiros como parâmetros,
representando horas (h), minutos (m) e segundos (s), e os converta em segundos. Ex:
relogio_segundos(2,40,10) = 9610 (2h, 40min e 10s correspondem a 9.610 segundos).
'''
def relogio_segundos(h,m,s):
    h = h*60*60
    m = m*60
    return h + m + s
#print(relogio_segundos(20,40,59))

'''3) Escreva uma função somaAte(n) que retorna a soma de todos os números naturais até e
incluindo o número n. Não utilize nenhum método pronto da linguagem Python para realizar a soma
automática. Ex:
somaAte(10) = 1 + 2 + 3 + 4 + … + 10 = 55'''

def soma(n):
    total = 0
    for i in range (1, n+1):
        total = total + i
    return total
#print(soma(5))

'''4) Crie uma função somaDivisores(n) que receba como parâmetro um valor inteiro positivo e
retorne a soma dos divisores desse valor. Ex:
somaDivisores(18) = 1 + 2 + 3 + 6 + 9 + 18 = 39'''

def somaDivisores(n):
    contador = 0
    for i in range(1,n+1):
        if (n%i ==0):
            contador += 1
            print(i, end = " , ")
    return(f"O número de divisores é: {contador}")
'''print(somaDivisores(15))
print(somaDivisores(1516546))
print(somaDivisores(169))'''

'''5) Crie um programa que receba três valores l1, l2 e l3 (obrigatoriamente maiores do que zero),
representando as medidas dos três lados de um triângulo. Seu programa deve conter duas funções:
• a função trianguloValido(l1,l2,l3) deve retornar um valor booleano indicando se esses
lados podem formar um triângulo válido (Dica matemática: um triângulo só pode ser
formado por três lados se cada um dos lados for menor que a soma dos outros dois)
• a função trianguloTipo(l1,l2,l3) deve retornar uma string que indique o tipo do
triângulo quanto aos seus lados:
◦ equilátero para caso os três lados sejam iguais;
◦ isósceles para caso dois lados sejam iguais e um diferente;
◦ escaleno caso os três lados sejam diferentes.
Obs1: A segunda função deve ser chamada apenas se a primeira determinar que os lados entrados
forma um triângulo válido.
Obs2: Nenhum print deve ser usado dentro das funções. Todas as mensagens exibidas na tela devem
estar no corpo principal do programa.'''
def triangulo(l1,l2,l3):
    if (l1<0 or l2 < 0 or l3 < 0):
        print("insira lados válidos")
    else:
        if ((l1 > l2 + l3 or l2 > l1 +l3 or l3 > l1 +l2)):
            print("Triângulo não obedece a condição de existência!")
        else:
            if l1 == l2 and l2 ==l3:
                print("triângulo equilátero")
            elif l1 == l2 and l2 != l3 or l1 == l3 and  l2 != l3 or l1 == l3 and l3 != l2:
                print("triângulo isórseles")
            elif l1 != l2 or l1 != l3 or l2 != l3:
                print("triângulo escaleno")
'''l1 = float(input( "insira o lado L1: "))
l2 = float(input( "insira o lado L2: "))
l3 = float(input( "insira o lado L3: "))
triangulo(l1,l2,l3)'''