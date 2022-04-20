'''12) Escreva um programa que leia os coeficientes a, b e c de uma equação do segundo grau
ax2 + bx + c e faça as seguintes verificações:
• se o coeficiente a for igual a zero, imprima a mensagem “Não é equação do segundo grau”
• se Δ<0 , não existe raiz real, então imprima a mensagem “Não existe raiz real.”
• se Δ=0 , existe uma raiz real, então imprima a mensagem “Raiz única.” e o valor dessa
raiz.
• se Δ>0 , existe duas raízes reais, então imprima a mensagem “Duas raízes.” e os valores
dessas raízes.
Lembrando que Δ=b
2−4 ac e as raízes da equação são dadas por: x=
−b±√Δ
2a.
'''
def sqrt(n):
    sgn = 0
    if n < 0:
        sgn = -1
        n = -n
    val = n
    while True:
        last = val
        val = (val + n / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    if sgn < 0:
        return complex(0, val)
    return val
a = float(input("Insira o coeficiente A: "))
b = float(input("Insira o coeficiente B: "))
c = float(input("Insira o coeficiente C: "))

delta = (b**2) - 4*(a*c)
x1 = (-b) + (sqrt(delta)/2*a)
x2 = (-b) - (sqrt(delta)/2*a)
if (delta < 0):
  print('Não existe raizes reais')
elif (delta == 0):
  print('Existe duas raizes de valores IGUAIS.')
elif(delta > 0):
  print(f"{x1} ,{x2}")
 