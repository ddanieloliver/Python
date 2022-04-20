'''14) Faça um programa que receba o código do produto comprado e a quantidade comprada do
produto. Calcule e mostre o preço unitário do produto comprado, segundo a Tabela I; o preço total
da nota; o valor do desconto, seguindo a Tabela II e aplicado sobre o preço total da nota; e o preço
final da nota depois do desconto.'''

produto = int(input("Insira o código do produto: "))
quant = float(input("Insira a quantidade do produto: "))

if  1 <= produto <= 10:
    preco = 10
elif  11 <= produto <= 20:
    preco = 15
elif  21 <= produto <= 30:
    preco = 20
elif  31 <= produto <= 40:
    preco = 30
else:
    print("Algo deu errado")

print(f"O preço do produto de código {produto} é R$ {preco}")
precoTotal = preco*quant

print(f"O valor da sua compra sem desconto é {precoTotal}")

if precoTotal <= 250:
    desconto = precoTotal * 5/100
elif 250 < precoTotal <= 500:
    desconto = precoTotal * 10/100
elif 500 < precoTotal:
    desconto = precoTotal * 15/100
else:
    print("Algo deu errado")

print(f"O valor do seu desconto é R${desconto}")

precoFinal = precoTotal - desconto

print(f"O preço final dessa nota é R${precoFinal}")