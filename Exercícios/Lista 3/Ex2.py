'''Dificuldades na rsolução e revisar'''


'''2) Escreva um programa que imprima a tabuada de um número N entre 1 e 9.'''

n = float(input("Insira o valor de n: "))

print("( 1 ) Soma")
print("( 2 ) Subtração")
print("( 3 ) Multiplicação")
print("( 4 ) Divisão")

operacao = float(input( "Insira a Operação: "))
if operacao == 1:
    for i in range(11):
        print (f"{n} + {i} = {n + i} ") # 5 + 0 = 5
        i =+ 1
elif operacao == 2:
    for i in range(11):
        print (f"{n} - {i} = {n - i} ") # 5 - 0 = 5
        i =+ 1
elif operacao == 3:
    for i in range(11):
        print (f"{n} * {i} = {n * i} ") # 5 + 0 = 5
        i =+ 1
elif operacao == 4:
    for i in range(1, 11):
        print (f"{n} / {i} = {n / i} ") # 5 + 0 = 5
        i =+ 1
else:
    print("Algo de errado não está certo...")

