'''
1) Faça um programa que receba dois números e diga o maior deles. Caso sejam iguais, o programa
deve ser capaz de informar isto.
'''

n1 = float(input('insira o primeiro número: '))
n2 = float(input('insira o segundo número: '))
if n1 == n2:
    print('Os números são iguais')

elif n1 < n2:
    print(f'O numero {n2} é maior')

elif n1 > n2:
    print(f'O numero {n1} é maior')

else:
    print('Insira um valor válido')
