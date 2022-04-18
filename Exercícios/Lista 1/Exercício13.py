'''
13) Escreva um programa que leia a altura e o raio da base de
um cilindro circular reto e escreva as seguintes informações:
área lateral, área da base e volume.

Comprimento da circunferência = 2π × raio
Área da circunferência = π × raio2
Volume do cilindro = Áreada base × Altura
'''

altura = float(input("Qual é o valor da altura?"))
raioDaBase = float(input("Qual o valor do raio da base?"))
PI = 3.14
comprimentoCircunferencia = 2* PI *raioDaBase
areaCircunferencia = PI * raioDaBase **2
volumeCilindro = areaCircunferencia * altura
areaLateral = comprimentoCircunferencia * altura
print( f'A área lateral é {areaLateral}')
print( f'A área da base é {areaCircunferencia}')
print( f'O volume do cilindro é {volumeCilindro}')
