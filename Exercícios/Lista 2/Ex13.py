'''13) Muitos supermercados vendem o mesmo produto com tamanhos e preços diferentes. Por
exemplo: Leite Ninho de 200g a R$5,00 e Leite Ninho de 1Kg a R$23,00. No caso deste exemplo, é mais vantajoso proporcionalmente para o cliente comprar o Leite Ninho de 1Kg. Escreva um programa que leia as gramas e preços de um determinado produto e retorne indicando a versão proporcionalmente mais barata ao cliente.
Ex:
produto: Leite Ninho
massa da versao 1: 200
preco da versao 1: 5
massa da versao 2: 1000
preco da versao 2: 23
Resultado: Leite Ninho de 1000g por R$23.00 eh mais vantajoso.'''

produto = str(input("Insira o produto: "))
massaDaVersao1 = float(input("Insira a quantidade do primeiro produto: "))
massaDaVersao2 = float(input("Insira a quantidade do segundo produto: "))

precoDaVersao1 = float(input("insira o preço do primeiro produto: "))
precoDaVersao2 = float(input("insira o preço do segundo produto: "))
print(f"{precoDaVersao1/massaDaVersao1} 1")
print(f"{precoDaVersao2/massaDaVersao2} 2")

if (precoDaVersao1/massaDaVersao1) < (precoDaVersao2/massaDaVersao2):
  print(f"o {produto} de {massaDaVersao1}g é mais vantajoso.")
elif (precoDaVersao1/massaDaVersao1) > (precoDaVersao2/massaDaVersao2):
  print(f"o {produto} de {massaDaVersao2}g é mais vantajoso.")
else:
  print("Os dois estão no mesmo preço ")