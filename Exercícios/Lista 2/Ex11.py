'''11) Dados três valores A, B e C, verificar se eles podem ser valores dos lados de um triângulo e, se
forem, verificar se é um triângulo escaleno, equilátero ou isósceles. Dicas:
• O lado de um triângulo não pode ser maior ou igual do que a soma dos outros dois.
• Um triângulo equilátero possui os três lados iguais.
• Um triângulo isósceles possui dois lados iguais.
• Um triângulo escaleno possui os três lados diferentes.'''

A = float(input("Insira o valor do lado A :"));
B = float(input("Insira o valor do lado B :"));
C = float(input("Insira o valor do lado C :"));

if A <= 0 or B <= 0 or C <= 0:
    print("Esse triângulo não existe!")

elif A >= B+C or B >= A+C or C >= B+A:
    print("Esse triângulo não existe!")
else: 
    print("Esse triângulo existe")

if A == B and B == C and C == A:
    print("Esse triângulo é equilátero!")
 
elif A != B and B != C and C != A:
    print("Esse triângulo é escaleno!")
    
else:
    print("Esse triângulo é isórcelis!")