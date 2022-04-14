'''2) Calcule o resultado das expressões, sabendo que A = 5, B = 10, C = – 8 e D = 1.5.
a) 2 * A % 3 – C == - 12
b) math.sqrt( – 2 * C) / 4 
c) ((20 / 3) / 3) + 8**2 / 2 
d) 5 * 3 + 15 % 5 + 8 – 1 * 20 / 15
e) math.sqrt( A**(A / B) ) + C * D
f) 5**2 – math.sqrt(125) * 0 / 540 – 10 / 2'''
import math
resultado = 2 * 5 % 3 - (-8) 

print (resultado)
resultado = math.sqrt( - 2 * (-8)) / 4

print (resultado)

resultado = math.sqrt( 5**(5 / 10) ) + (-8) * 1.5

print (resultado)

resultado = ((20 / 3) / 3) + 8**2 / 2

print (resultado)
resultado = (5 * 3) + (15 % 5) + 8 - (1 * 20 / 15)

print (resultado)
resultado = 5**2 - (math.sqrt(125) * 0 )/ 540 - (10 / 2)
print (resultado)

