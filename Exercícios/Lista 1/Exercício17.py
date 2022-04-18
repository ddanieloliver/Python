'''17) Muitos bancos possuem o serviço do crédito rotativo do cartão de crédito. Ele é um serviço que
pode ser acionado pela pessoa que não pode pagar o valor total da fatura no vencimento, mas não
quer ficar inadiplente. Para usar o crédito rotativo, o consumidor paga qualquer valor entre o
mínimo e o total da fatura. O restante é lançado no mês seguinte, com juros. Muitos bancos cobram
o valor de 3,3% de juros neste serviço. Escreva um programa que leia o valor usado por um cliente
no mês de Março, o valor que ele pagou dessa fatura, o valor usado por este cliente no mês de Abril
e retorne o valor da fatura do mês de Abril.
Ex:
Valor usado no mês de Março: 200
Valor pago no mês de Março: 20
Valor usado no mês de Abril: 150
Fatura do mês de Abril: 150 + 180 + 180*(3,3%) = 335,94'''

valorUsadoMesPassado = float(input('Qual o valor que foi usado mês passado?'))
valorPago = float(input("Quanto você pagou?"))
valorUsadoMesAtual = float(input('Qual o valor que foi usado esse mês?'))

faturaDesseMes = valorUsadoMesAtual + (valorUsadoMesPassado - valorPago) + ((valorUsadoMesPassado - valorPago) * 3.3/100)

print(f'O valor a pagar esse mês é {faturaDesseMes}')