'''Escreva um programa que leia as coordenadas (x,y) de um ponto e informe a qual quadrante ele
pertence segundo a figura abaixo.'''

x = float(input("Insira o valor de x: "))
y = float(input("Insira o valor de y: "))

if x > 0 and y > 0:
    print("Primeiro quadrante")
elif x < 0 and y > 0:
    print("Segundo quadrante")
elif x < 0 and y < 0:
    print("Terceiro quadrante")
elif x > 0 and y < 0:
    print("Quarto quadrante")
else:
    print("Alguma coisa deu errado")