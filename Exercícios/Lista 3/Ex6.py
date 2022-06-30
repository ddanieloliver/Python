'''6) Repita as questões 3 e 4, mas dessa vez continue lendo valores inteiros até que o usuário entre
com um número negativo.'''

m = 0
while True:
    n = int(input("Insira o valor de n: "))
    if n > 0:
        m = m + n
    else:
        break
print(m)

m = 0
while True:
    n = int(input("Insira o valor de n: "))
    if n > 0:
        if n > m:
            m = n

    else:
        break
print(m)
'''m = 0
for i in range(x):
    n = int(input("Insira o valor de n: "))
    if  n > m:
        m = n
    i =+ 1
print(m)'''
