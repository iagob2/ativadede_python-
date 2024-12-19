# Solicita ao usuário o número de alunos a serem cadastrados
n = int(input('Quantos alunos serão cadastrados? '))

# Inicializa o dicionário para armazenar os alunos
alunos = {}  # Dicionário para armazenar os alunos

# Cadastro de alunos
for c in range(n):
    # Coleta os dados de cada aluno
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2  # Calcula a média

    # Define a situação do aluno com base na média
    if media >= 7:
        situacao = 'aprovado'
    elif 5 <= media < 7:
        situacao = 'recuperação'
    else:
        situacao = 'reprovado'

    # Armazena os dados do aluno no dicionário
    alunos[nome] = {
        'nota1': nota1,
        'nota2': nota2,
        'media': media,
        'situacao': situacao
    }

# Exibe os dados dos alunos cadastrados
print('-=' * 20)
print(f'{"NOTAS DOS ALUNOS":^40}')
print('-=' * 20)
for nome, dados in alunos.items():
    print(f'Nome: {nome}, Nota 1: {dados["nota1"]}, Nota 2: {dados["nota2"]}, Média: {dados["media"]:.2f}, Situação: {dados["situacao"]}')
