from datetime import datetime  

# Inicializa as listas e dicionários
dados = {}  # Dicionário para armazenar temporariamente os dados de cada pessoa
pessoas = []  # Lista para armazenar todas as pessoas cadastradas

# Loop para cadastro de pessoas
while True:
    # Coleta os dados da pessoa
    dados['nome'] = str(input('Digite o seu nome: ')).strip().title()
    nasc = int(input('Digite o ano de nascimento: '))
    dados['sexo'] = str(input('Digite seu sexo [F/M]: ')).strip().upper()
    dados['idade'] = datetime.now().year - nasc  # Calcula a idade com base no ano atual

    # Adiciona os dados à lista principal e limpa o dicionário para o próximo cadastro
    pessoas.append(dados.copy())
    dados.clear()

    # Pergunta se o usuário deseja continuar
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

# Exibe o total de pessoas cadastradas
print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')

# Calcula a média de idade
soma_idades = sum(p['idade'] for p in pessoas)
media = soma_idades / len(pessoas)
print(f'A média de idade das pessoas cadastradas é: {media:.2f} anos.')

# Lista de mulheres cadastradas
print('\nLista de mulheres cadastradas:')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'- {p["nome"]}')

# Lista de pessoas acima da média de idade
print('\nLista de pessoas com idade acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print(f'- {p["nome"]} ({p["idade"]} anos)')
