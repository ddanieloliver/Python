'''5) Crie um programa que permita fazer a conversão cambial entre Dólares e Reais. Considere como
taxa de câmbio US$ 1,00 = R$ 3,92. Leia um valor em Dólares pelo teclado e mostre o
correspondente em Reais.'''

valor = float(input("digite o valor"))
moeda = str(input("digite a moeda"))
if moeda == "dolar":
    valor_real = valor / 3.92
    print(f"O valor em reais é: {valor_real}")
else:
    valor_dolar = valor*3.92
    print(f"O valor em Dolar é: {valor_dolar}")

