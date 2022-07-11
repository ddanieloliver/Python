'''3) Construa um dicionário que armazene dados de um aluno com nome, número de matrícula e
curso. Leia do usuário a informação de 50 alunos, armazene esses dados em uma lista e imprima-os
na tela.
'''
ALUNOS = 50
dadosAlunos = []
for i in range (ALUNOS):
    aluno = {
        'nome': str(input("Insira o nome do novo aluno: ")),
        'matricula': str(input("Insira a matrícula do aluno: ")),
        'curso': str(input("Insira o curso do aluno: "))
    }
    dadosAlunos.append(aluno)

print(dadosAlunos)