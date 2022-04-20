'''8) Faça um programa que receba três números inteiros e retorne o maior número dentre os três.'''

n1 = float(input('Insira o primeiro número'))
n2 = float(input('Insira o segundo número'))
n3 = float(input('Insira o terceiro número'))

if n1 > n2 >n3:
    print(f'O número {n1} é maior')
elif n1 > n3 >n2:
    print(f'O número {n1} é maior')
elif n2 > n1 >n3:
    print(f'O número {n2} é maior')
elif n2 > n3 >n1:
    print(f'O número {n2} é maior')
elif n3 > n2 >n1:
    print(f'O número {n3} é maior')
elif n3 > n1 >n2:
    print(f'O número {n3} é maior')
else:
    print("Os números são iguais")