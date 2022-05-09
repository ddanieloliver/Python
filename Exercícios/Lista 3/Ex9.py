#9) Escreva um programa que receba um número N e mostre todos os divisores de N.
n = int(input("Digite o número: "))
for i in range (1,n+1):
    if n%i==0:
        print(i)
