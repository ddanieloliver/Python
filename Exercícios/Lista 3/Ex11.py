#13) Escreva um programa que construa uma progressão aritmética a partir do valor inicial, da razão
#e da quantidade de elementos. Dica: em uma progressão aritmética, cada elementos é igual ao
#anterior somado com a razão.
vi = int(input("Digite o valor inicial: "))
r = int(input("Digite a razão: "))
qe = int(input("Digite a quantidade de elementos: "))

for i in range (qe):
    print(vi)
    vi = vi+r


    
    