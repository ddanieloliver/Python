'''
14) Escreva um programa que leia as coordenadas (x,y) de um ponto e retorne a sua distância até a
origem do sistema de coordenadas.
'''
from math import sqrt
x = float(input("Digite a cordenada x: "))
y= float(input("Digite a cordenada y: "))

distancia = sqrt(x**2+y**2)
print(f"a distancia é {distancia}")

