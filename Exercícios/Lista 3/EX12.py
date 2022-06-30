'''12) Escreva um programa que receba um número N e informe se N é um número primo ou não.'''

def ePrimo(n):
  contadorDeDivisores = 0
  for i in range (1, n+1):
    if n % i == 0:
      contadorDeDivisores += 1
  print(f"O número de divisores é {contadorDeDivisores}") 
  if contadorDeDivisores ==2:
    print("É Primo")
  else: print("Não é primo")
#n = int(input("Insira um número: "))
#ePrimo(n)