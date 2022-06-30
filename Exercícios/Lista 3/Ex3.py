'''3) Escreva um programa que leia 10 números inteiros e retorne o valor máximo inserido.'''
m = 0
for i in range(10):
    n = int(input("Insira o valor de n: "))
    if  n > m:
        m = n
    i =+ 1
    
print(m)