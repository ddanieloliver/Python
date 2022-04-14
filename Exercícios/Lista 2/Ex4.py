'''
4) Faça um programa que leia 3 notas, verifique se as notas são válidas (um valor entre 0 e 10) e
exiba na tela a média dessas notas em duas casas decimais. Se pelo menos uma das notas não for
válida, a média não é calculada e uma mensagem de erro deve ser exibida.
'''

nota1 = float(input('Insira a primeira nota'))
nota2 = float(input('Insira a segunda nota'))
nota3 = float(input('Insira a terceira nota'))

if 0 < nota1 < 10 and 0 < nota2 < 10 and 0 < nota3 < 10: 
    print ((f'a sua média é { (nota1+nota2+nota3)/3}'))
else:
    print('Alguma nota está inválida')