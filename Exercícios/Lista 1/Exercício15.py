'''Escreva um programa que leia as coordenadas de dois pontos e retorne a distância entre eles'''
import math

xa = float(input('Digite o x do ponto A'))
ya = float(input('Digite o y do ponto A'))
xb = float(input('Digite o x do ponto B'))
yb = float(input('Digite o y do ponto B'))

AB = math.sqrt((xb - xa)**2 + (yb - ya)**2)

print(f'A distância entre os dois pontos é {AB}')