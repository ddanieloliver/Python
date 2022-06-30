'''8) Escreva um programa que retorne a soma de todos os números ímpares positivos menores do um
valor N entrado pelo usuário.'''
n = int(input("Insira o número"))
resultado = 0
for i in range(n+1):
    if i % 2 != 0:
        resultado += i
        
print(resultado)
