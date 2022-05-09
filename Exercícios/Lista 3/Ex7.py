'''7) Escreva um programa que leia um valor N positivo e retorne o fatorial de N.'''
n = int(input("Insira o valor de N: "))
fatorial = 1
for i in range (1, n+1 ):
    fatorial = fatorial * i
    i += 1
print(fatorial)