import random

alunos = []  # Lista vazia para armazenar os nomes dos alunos

# Utilizando um loop for para solicitar os nomes dos alunos
for i in range(1, 5):  # i variará de 1 a 4 (inclusive)
    nome = input(f'Informe o nome do Aluno {i}º: ')
    alunos.append(nome)  # Adiciona o nome do aluno à lista

print('\n--- Sorteando ordem de apresentação ---\n')
random.shuffle(alunos)
for idx, aluno in enumerate(alunos, start=1):
    print(f' {idx}: {aluno}')