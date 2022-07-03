'''2) Escreva uma função palindromo(s) que retorna verdadeiro ou falso, caso a string entrada seja
um palíndromo. (Palíndromos são palavras ou frases que são iguais tanto da esquerda pra direita
como da direita pra esquerda).Ex:
palindromo("bemtevi") False →
palindromo("arara") True '''

s = str(input("Insira o susoeito palindromo: "))

def ePalindromo(string):
    if string[::-1] == string[::1]:
        print("É palindromo!")
    else:
        print("Não é!")
ePalindromo(s)