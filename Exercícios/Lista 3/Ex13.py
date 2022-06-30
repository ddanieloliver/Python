'''13) Escreva um programa que construa uma progressão aritmética a partir do valor inicial, da razão
e da quantidade de elementos. Dica: em uma progressão aritmética, cada elementos é igual ao
anterior somado com a razão'''
    
def criarPA(a1, n, r):

  for i in range(0, n):
    a = a1 + i * r 
    print(f"{a} ", end = '')
a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
n = int(input("Digite o número de termos da PA: "))
criarPA(a1, n, r)
