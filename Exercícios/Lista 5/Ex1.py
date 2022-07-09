'''1) Escreva uma função inverte(s) que recebe uma string s e retorna a os caracteres da string de
trás para frente. Não use a função reverse da linguagem Python. Ex:
inverte("Russas") "sassuR" '''



'''def inverte(string):
    s_invertida = ""
    for i in range (len(string)):
        s_invertida = s_invertida + string[len(string) -i -1]    
    print ( s_invertida)
s = str(input( 'insira a string que deseja inverter: '))
inverte(s)
'''

def inverter(string):
    return string[::-1]

print(inverter('Russas'))