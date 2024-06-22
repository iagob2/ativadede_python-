import random

alunos = []  # Lista vazia para armazenar os nomes dos alunos

# Utilizando um loop for para solicitar os nomes dos alunos
for i in range(1, 5):  # i variará de 1 a 4 (inclusive)
    nome = input(f'Informe o nome do Aluno {i}º: ')
    alunos.append(nome)  # Adiciona o nome do aluno à lista

print('\n--- Aluno sorteado ---\n')
aluno_escolhido = random.choice(alunos)
print(f'O aluno escolhido para apagar o quadro foi ***{aluno_escolhido}***\n')
