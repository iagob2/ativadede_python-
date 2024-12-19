jogador = dict()

# Coleta o nome do jogador
jogador['nome'] = str(input('Nome do Jogador: '))

# Coleta o número de partidas jogadas
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

# Criando a lista de gols para cada partida
jogador['gols'] = [int(input(f'Quantos gols na partida {i+1}? ')) for i in range(tot)]


# Calcula o total de gols
jogador['total'] = sum(jogador['gols'])


print('-=' * 30)

# Exibe os gols por partida
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'  => Na partida {i + 1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
