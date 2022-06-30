'''14) Escreva um programa que apresente um menu de opções para cálculo das seguintes operações
entre dois números:
1. adição
2. subtração
3. multiplicação
4. divisão
5. saída
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a
volta do menu de opções. O programa só termina quando for escolhido a opção de saída (opção 5).
'''
def operacao():
  def soma(x,y):
    print(f"O resultado é {x+y}")
  def subtracao(x,y):
    print(f"O resultado é {x-y}")
  def divisao(x,y):
    print(f"O resultado é {x/y}")
  def multiplicacao(x,y):
    print(f"O resultado é {x*y}")
  
  
  while True:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o outro número: "))
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    print("[5] - Saída")
    op = int(input("Digite a operação:"))
    if op == 1:
      soma(n1,n2)
    elif op == 2:
      subtracao(n1,n2)
    elif op == 3:
      multiplicacao(n1,n2)
    elif op == 4:
      divisao(n1,n2)
    elif op == 5:
      break
    else:
      print("ERRO! Digite uma opção válida")
operacao()