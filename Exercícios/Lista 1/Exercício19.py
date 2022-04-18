'''Faça um programa que leia um número inteiro positivo de três dígitos e imprima o número
formado pelos dígitos invertidos do número lido. Ex: Número lido = 123 → Número escrito = 321.'''

num = input("Insira um número inteiro e positivo de 4 dígitos") 
revertido = num[::-1]
print(revertido)