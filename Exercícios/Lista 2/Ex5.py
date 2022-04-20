'''
5) Crie uma versão do programa da questão 4 de forma que informe se o aluno está aprovado
(média maior ou igual a 7), reprovado (média menor do que 4) ou em recuperação (média maior ou
igual a 4 e menor do que 7).
'''
nota1 = float(input('Insira a primeira nota'))
nota2 = float(input('Insira a segunda nota'))
nota3 = float(input('Insira a terceira nota'))
media = (nota1+nota2+nota3)/3

if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10: 
    print ((f'a sua média é { (nota1+nota2+nota3)/3}'))
    if media <4:
        print ('Reprovado!!!')
    elif 4 < media < 7:
        print ('are you ready for the recuperation?' )
    else:
        print ('Aprovrado!')
else:
    print('Alguma nota está inválida')