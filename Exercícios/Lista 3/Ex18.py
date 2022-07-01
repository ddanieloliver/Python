'''18) Estudiosos já formularam diversas séries matemáticas que, se levadas ao infinito, podem calcular π de
forma precisa em inúmeras casas decimais. Algumas delas são tão complexas que só conseguem ser
analisadas por supercomputadores. A de Gregory-Leibniz, por sua vez, é uma das mais simples. Para isso,
usa-se a seguinte fórmula:
π=4/1−4/3+4/5−4/7+4/9−4/11+4/13−4/15⋯
Somas e subtrações são alternadas com frações de numerador 4 e denominador com números ímpares em
sequência. Quanto mais longe for, mais perto este resultado será de π . Escreva um programa que leia do
usuário uma quantidade positiva N de parcelas da sequência de Gregory-Leibniz e retorne a aproximação do
valor de π .
'''
n = int(input("Insira o numero de parcelas: "))
PIsobre4 = 1
for i in range (1, n+1, 1):
    for j in range(n, 0, -2 ):
        PI = PI + 4/i - 2*(4/j)
print(PI)