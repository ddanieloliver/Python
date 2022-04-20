'''6) Uma universidade avalia seus cursos através de diversos fatores e atribui uma nota de 0 a 10 ao
final da avaliação. Para fins de divulgação, os cursos são classificados segundo uma classificação
descrita na tabela abaixo:
Escreva um programa que converta a nota de um curso em seu conceito.'''

media = int(input('Insira sua média: '))
if 8 <= media <= 10:
  print( 'Curso de conceito "A"')
elif 7 <= media < 8:
  print( 'Curso de conceito "B"')
elif 6 <= media < 7:
  print( 'Curso de conceito "C"')
elif 5 <= media < 6:
  print( 'Curso de conceito "D"')
elif 0 <= media < 5:
  print( 'Curso de conceito "E"')
else:
  print('Algum erro aconteceu... :/')