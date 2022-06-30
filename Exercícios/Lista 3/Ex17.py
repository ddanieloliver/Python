'''17) Na matemática, o número harmônico designado por H (n) define-se como sendo a soma da série
harmônica:
H (n)=1+ 1/1 + 1/2 + 1/3 + ⋯ + 1/n
Faça um programa que leia um valor n inteiro positivo e calcule o valor de H (n) .'''

n = int(input("insira o valor: "))

if(n==0):
    print("Número inválido!")
resultado = 1
for i in range (1, n+1):
        resultado += 1/i
print(resultado)