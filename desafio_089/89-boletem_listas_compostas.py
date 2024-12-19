# Solicita ao usuário o número de alunos a serem cadastrados
aluno = int(input('Quantos alunos serão cadastrados? '))

# Inicializa as listas
dados = []  # Lista temporária para armazenar os dados de um aluno
alunos = []  # Lista para armazenar todos os alunos

# Cadastro de alunos
for c in range(aluno):
    # Coleta os dados de cada aluno
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2  # Calcula a média

    # Adiciona os dados do aluno na lista temporária
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    dados.append(media)

    # Adiciona os dados do aluno na lista principal e limpa a temporária
    alunos.append(dados[:])  # Adiciona uma cópia dos dados
    dados.clear()  # Limpa a lista temporária para o próximo aluno

# Exibe os dados dos alunos cadastrados
print('-=' * 20)
print(f'{"NOTAS DOS ALUNOS":^40}')
print('-=' * 20)
for i, aluno in enumerate(alunos, 1):
    print(f'Aluno {i}: Nome: {aluno[0]}, Nota 1: {aluno[1]}, Nota 2: {aluno[2]}, Média: {aluno[3]:.2f}')
