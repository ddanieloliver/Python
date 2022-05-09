'''5) Repita as questões 3 e 4, mas no início do programa, pergunte pro usuário quantos números ele
irá entrar e leia essa quantidade de números inteiros.'''
x = int(input("Com quantos números desejas entrar? "))
m = 0
for i in range(x):
    n = int(input("Insira o valor de n: "))
    m = m + n
    i =+ 1
print(m)


m = 0
for i in range(x):
    n = int(input("Insira o valor de n: "))
    if  n > m:
        m = n
    i =+ 1
print(m)
