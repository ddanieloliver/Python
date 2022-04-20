'''Escreva um programa que receba do usuário as coordenadas (x,y) de três pontos A, B e C e faça
o que se pede:
• Verifique se os pontos A e B podem formar um retângulo como mostrado na figura abaixo,
ou seja, o ponto A ser um canto inferior esquerdo e B um canto superior direito de um
retângulo. O programa deve informar se isto é possível.
• Caso o retângulo seja possível, informe se o ponto C é interno ao retângulo ou não.'''

Xa = int(input("Insira o valor de X do ponto A"))
Ya = int(input("Insira o valor de Y do ponto A"))
Xb = int(input("Insira o valor de X do ponto B"))
Yb = int(input("Insira o valor de Y do ponto B"))
Xc = int(input("Insira o valor de X do ponto C"))
Yc = int(input("Insira o valor de Y do ponto C"))

if Xa > Xb:
    print("Esses pontos não atendem aos requisitos para a construção do retângulo")
elif Ya > Yb or Ya != Yb:
    print("Esses pontos não atendem aos requisitos para a construção do retângulo")
else:
    print("Fazendo retângulo...")
    if Yc < Yb and Yc > Ya and Xc < Xb and Xc > Xa:
        print("O ponto C está dentro do retangulo")
    else: 
        print("O ponto C está fora do retângulo")