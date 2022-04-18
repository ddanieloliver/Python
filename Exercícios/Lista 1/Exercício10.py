'''
10) Escreva um programa que leia os coeficientes A, B, e C e um valor x e retorne o resultado de
sua aplicação na função f (x)=Ax2+Bx+C .
'''

A = int(input("Insira o Coeficiênte a: "))
B = int(input("Insira o Coeficiênte b: "))
C = int(input("Insira o Coeficiênte c: "))
x = int(input('Insira o valor de x: '))

y = A*(x**2) + B*x + C

print('f(x) = Ax2 + Bx + C')
print( f'f(x) = {y}')