'''16) Faça um programa que receba o valor do salário-base e o número de dependentes de um
determinado funcionário e calcule e mostre o salário a receber do funcionário de acordo com as
regras a seguir:
• Para cada dependente, acrescentar R$120,00.
• O salário bruto é igual ao salário-base mais o valor dos dependentes.
• Calcular o valor do imposto de renda retido na fonte (IRRF) de acordo com a tabela:
IRRF Salário Bruto
Isento Inferior a R$1000,00
10% De R$1000,00 até R$ 2500,00
20% Superior a R$2500,00
• O salário líquido é igual ao salário bruto menos o IRRF.
• A gratificação é de acordo com a tabela a seguir:
Salário Líquido Gratificação
Até R$1750,00 R$ 500,00
Superior a R$1750,00 R$ 250,00
• O salário a receber do funcionário é igual ao salário líquido mais a gratificação.'''

salarioBase = int(input("Insira o salário base: "))
dep = int(input('Insira o número de dependentes: '))
salarioBruto = salarioBase + (dep * 120)
salarioLiquido = salarioBruto - IR

if 1000 <= salarioBruto <= 2500:
  print(f"Imposto de renda igual a 10% de {salarioBruto} = {salarioBruto *(10/100)}")
elif salarioBruto < 1000:
  print('Insento.')
elif salarioBruto > 2500:
  print(f"Imposto de renda igual a 20% de {salarioBruto} = {salarioBruto *(20/100)}")
else:
  print("Algo deu errado")

