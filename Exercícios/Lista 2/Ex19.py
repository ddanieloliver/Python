'''19) Escreva um programa que receba do usuário as coordenadas (x,y) de três pontos A, B e C e
calcule a altura e a largura do retângulo circunscrito como mostrado na figura abaixo.'''

Xa = int(input("Insira o valor de X do ponto A"))
Ya = int(input("Insira o valor de Y do ponto A"))
Xb = int(input("Insira o valor de X do ponto B"))
Yb = int(input("Insira o valor de Y do ponto B"))
Xc = int(input("Insira o valor de X do ponto C"))
Yc = int(input("Insira o valor de Y do ponto C"))


if Xa > Xb > Xc or Xa > Xc > Xb:
    largura = Xa
elif Xb > Xa > Xc or Xb > Xc > Xa:
    largura = Xb
elif Xc > Xb > Xa or Xc > Xa > Xb:
    largura = Xc
else:
    print("Alguma coisa deu errado...")

if Ya > Yb > Yc or Ya > Yc > Yb:
    altura = Ya
elif Yb > Ya > Yc or Yb > Yc > Ya:
    altura = Yb
elif Yc > Yb > Ya or Yc > Ya > Yb:
    altura = Yc
else:
    print("Alguma coisa deu errado...") 

area = altura * largura 

print(f"A area do retângulo circunscrito é {area}")