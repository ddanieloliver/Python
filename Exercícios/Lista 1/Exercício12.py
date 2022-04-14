'''
12) Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula da conversão é
R=G⋅(π /180) , sendo G o ângulo em graus e R em radianos. (Obs: defina uma constante para o
valor de π ).
'''
G = int(input("Digite o valor do ângulo em graus"))
pi = 3.14
R = G*(pi/180)

print(f"o valor do angulo em radianos é {R}")
