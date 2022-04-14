'''
1) Faça um programa que receba dois números e diga o maior deles. Caso sejam iguais, o programa
deve ser capaz de informar isto.
'''

numero1 = (input('insira o primeiro número: '))
numero2 = (input('insira o segundo número: '))
if numero1.isnumeric() == True and numero2.isnumeric() == True: 

    if numero1 == numero2:
        print( 'Os números são iguais')
    elif numero1 > numero2:
        print( f'O numero {numero1} é maior')
    else:
        print( f'O numero {numero2} é maior')
else:
    print('insira um número válido')
'''A validação não ocorre da forma correta,
 não está indentificando números menores/'''