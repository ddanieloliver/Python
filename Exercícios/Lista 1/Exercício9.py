'''
9) Escreva um programa que leia os coeficientes A, B e C de uma equação Ax2
+Bx+C=0 e calcule
o valor do discriminante delta e as raízes da equação.

'''
from math import sqrt
a = int(input("Digite o coeficiente A: "))
b = int(input("Digite o coeficiente B: "))
c = int(input("Digite o coeficiente C: "))

delta = (b**2)-(4*a*c)

x1 = ((-b) + (sqrt(delta)))/2*a
x2 = ((-b) - (sqrt(delta)))/2*a

print(f"o valor de delta é:{delta}")
print(f"o valor das raízes é:{x1} e {x2}")