'''10) Escreva um programa tenha o seguinte menu de opções:
1. soma
2. subtração
3. multiplicação
4. divisão
O usuário deve ser capaz de escolher uma dessas opções digitando o número correspondente e
depois inserir os valores a serem usados na operação desejada. Depois o programa escreve a
resposta.'''

print("1. soma")
print("2. subtração")
print('3. multiplicação')
print("4. divisão ")

valor1 = float(input("Insira o primeiro valor: "))
valor2 = float(input("Insira o segundo valor: "))
operacao = str(input("insira a operação: "))

if operacao == "soma":
    print(valor1 + valor2)
elif operacao == "multiplicação":
    print(valor1*valor2)
elif operacao == "subtração":
    print(valor1-valor2)
elif operacao == "divisão":
    print(valor1/valor2)