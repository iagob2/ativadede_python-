# Tupla com os 20 primeiros colocados do Campeonato Brasileiro (exemplo fictício)
times = (
    'Botafogo', 'Palmeiras', 'Flamengo', 'Atlético-MG', 'Grêmio', 
    'São Paulo', 'Internacional', 'Fluminense', 'Fortaleza', 'Athletico-PR', 
    'Cruzeiro', 'Corinthians', 'Santos', 'Bahia', 'Cuiabá', 
    'Goiás', 'Vasco', 'Coritiba', 'América-MG', 'Red Bull Bragantino'
)

# Exibindo a tupla completa
print('Times do Campeonato Brasileiro 2024:')
for pos, time in enumerate(times, start=1):  # Exibe todos os times com suas posições
    print(f'{pos}º - {time}')

# Exibindo os 5 primeiros colocados
print('\nOs 5 primeiros colocados são:')
for c in range(0, 5):  # Itera sobre os primeiros 5 times
    print(f'{c+1}º - {times[c]}')

# Exibindo os 4 últimos colocados
print('\nOs 4 últimos colocados são:')
for c in range(-4, 0):  # Itera sobre os últimos 4 times usando índices negativos
    print(f'{len(times) + c + 1}º - {times[c]}')

# Exibindo os times em ordem alfabética
print('\nTimes em ordem alfabética:')
for time in sorted(times):  # Ordena os times alfabeticamente
    print(time)

# Verificando a posição de um time específico
time_procurado = 'Flamengo'  # Substitua pelo time desejado
posicao = times.index(time_procurado) + 1  # Encontra o índice do time e ajusta para posição (começa em 1)
print(f'\nO time {time_procurado} está na {posicao}ª posição.')
