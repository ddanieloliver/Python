'''4) Usando os operadores aritméticos, relacionais e lógicos da linguagem C e supondo que há duas
constantes true e false que simulam valores booleanos, determine os resultados obtidos na
avaliação das expressões lógicas seguintes.
Obs: Os valores das variáveis são: A = 2, B = 7, C = 3.5 e L = false.
a) B == A * C and L or true
b) B > A or B == A**A
c) L and B / A >= C or not A <= C
d) not L or true and math.sqrt(A+B) >= C
e) L or B**A <= C * 10 + A * B
'''
from math import sqrt

A = 2
B = 7
C = 3.5 
L = False


print(B == A * C and L or True)
print( B > A or B == A**A)
print(False and B / A >= C or not A <= C)
print(not L or True and math.sqrt(A+B) >= C)
print(L or B**A <= C * 10 + A * B)