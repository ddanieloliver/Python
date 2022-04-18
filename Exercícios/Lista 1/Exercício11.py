'''
11) Escreva um programa que leia os dois catetos de um triângulo retângulo e retorne o valor da
hipotenusa.
'''
from math import sqrt


a = int(input( "insira o valor do cateto A"))
a2 = a**2
b = int(input( "insira o valor do cateto B"))
b2 = b**2

c = sqrt(a2 + b2)

print(f'O valor da hipotenusa é {c}')