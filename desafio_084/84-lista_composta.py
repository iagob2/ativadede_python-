# Listas para armazenar os dados temporários e as pessoas cadastradas
dado = []
pessoa = []

while True:
    # Solicita os dados do usuário
    nome = input('Digite o seu nome: ')
    peso = float(input('Digite o peso da pessoa: '))

    # Adiciona o nome e o peso à lista temporária
    dado.append(nome)
    dado.append(peso)

    # Copia os dados para a lista principal e limpa a lista temporária
    pessoa.append(dado[:])
    dado.clear()

    # Pergunta ao usuário se deseja continuar
    r = input('Quer continuar? [S/N]: ').strip().upper()
    if r == 'N':  # Sai do loop se a resposta for 'N'
        break

# Exibe o número de pessoas cadastradas
print(f'\nForam cadastradas {len(pessoa)} pessoas.')

# Inicializa as variáveis para o peso mais pesado e mais leve
maisPesada = pessoa[0][1]
maisLeve = pessoa[0][1]

# Descobre os pesos mais pesado e mais leve
for p in pessoa:
    if p[1] > maisPesada:
        maisPesada = p[1]
    if p[1] < maisLeve:
        maisLeve = p[1]

# Exibe os resultados
print(f'\nO maior peso foi {maisPesada:.1f}kg. Peso de ', end='')
for p in pessoa:
    if p[1] == maisPesada:
        print(f'[{p[0]}] ', end=' ')
        
print(f'\nO menor peso foi {maisLeve:.1f}kg. Peso de ', end='')
for p in pessoa:
    if p[1] == maisLeve:
        print(f'[{p[0]}]', end=' ')
