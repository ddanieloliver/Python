'''6) Seja a seguinte lista: minha_lista = [76, 92.3, "oi", True, 4, 76]. Após criar essa lista,
faça o que se pede abaixo:
1. Insira a string “pêra” e o número 76 no final da lista
2. Insira a string “gato” na posição 3 da lista
3. Insira o número 99 no início da lista
4. Escreva o índice onde a string “oi” se encontra dentro da lista
5. Conte quantas vezes o número 76 aparece na lista
6. Remova a primeira ocorrência do número 76 da lista
7. Descubra onde o número 4 está na lista e o remova.
'''

minha_lista = [76, 92.3, "oi", True, 4, 76]

minha_lista.append("pera")
minha_lista.append(76)
minha_lista[2:2] = ['gato']
minha_lista[0:0] = [99]
print(minha_lista.index("oi")) # o method index equivale ao metodo find de strings

contador = 0
for i in minha_lista :
    if i == 76:
        contador += 1
print (contador)

deletar = minha_lista.index(76)

del minha_lista[deletar]
print(minha_lista)

deletar4 = minha_lista.index(4)
print(deletar4)
del minha_lista[deletar4]
print(minha_lista)