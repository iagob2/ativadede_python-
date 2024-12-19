# Inicializa os dicionários
jogador = dict()  # Dicionário para armazenar os dados temporários de cada jogador
jogadores = dict()  # Dicionário para armazenar todos os jogadores

# Solicita o número de jogadores
tot_jogadores = int(input('Quantos jogadores serão cadastrados? '))

# Loop para cadastrar cada jogador
for c in range(tot_jogadores):
    # Coleta o nome do jogador
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()

    # Coleta o número de partidas jogadas
    tot_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    # Cria a lista de gols para cada partida
    jogador['gols'] = [int(input(f'  Quantos gols na partida {i + 1}? ')) for i in range(tot_partidas)]

    # Calcula o total de gols
    jogador['total'] = sum(jogador['gols'])

    # Adiciona o jogador ao dicionário principal
    jogadores[f'jogador {c + 1}'] = jogador.copy()

    # Limpa o dicionário temporário para o próximo jogador
    jogador.clear()

# Exibe os dados de todos os jogadores
print('-=' * 30)
for nome, dados in jogadores.items():
    print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
    for i, g in enumerate(dados['gols']):
        print(f'  => Na partida {i + 1}, fez {g} gols.')
    print(f'Total de gols: {dados["total"]}.')
    print('-=' * 30)

