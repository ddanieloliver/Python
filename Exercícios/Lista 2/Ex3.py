'''
3) Faça um programa que receba dois números inteiros A e B e informe que A é múltiplo de B ou
não.
'''
A = int(input("Digite um número inteiro: "))

B = int(input("Digite outro número inteiro: "))
if A%B == 0 :
    print("o número é divisível")
else :
    print("o número não é divisível")