'''9) Escreva um programa que receba três números e escreva eles em ordem crescente.'''
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 < n2 <=n3:
    print(f'{n1}, {n2}, {n3}')
elif n1 < n3 <=n2:
     print(f'{n1}, {n3}, {n2}')
elif n2 < n1 <=n3:
    print(f'{n2}, {n1}, {n3}')
elif n2< n3 <=n1:
     print(f'{n2}, {n3}, {n1}')
elif n3 < n2 <=n1:
     print(f'{n3}, {n2}, {n1}')
elif n3 < n1 <=n2:
     print(f'{n3}, {n1}, {n2}')
     
elif n1 > n2 >=n3:
    print(f'{n3}, {n1}, {n2}')
elif n1 > n3 >= n2:
   print(f'{n2}, {n3}, {n1}')
elif n2 > n1 >= n3:
    print(f'{n3}, {n1}, {n2}')
elif n2 > n3 >= n1:
    print(f'{n1}, {n3}, {n2}')
elif n3 > n2 >= n1:
     print(f'{n1}, {n2}, {n3}')
elif n3 > n1 >=n2:
    print(f'{n2}, {n1}, {n3}')
else:
    print("Os números são iguais")