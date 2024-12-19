from random import randint

# Solicita ao usuário o número de jogos a serem gerados
num = int(input('Quantos jogos serão gerados? '))

# Inicializa as listas
numeros = []  # Lista para armazenar os números de um único jogo
lista = []  # Lista para armazenar todos os jogos

# Gera os jogos
for n in range(num):
    while len(numeros) < 6:  # Garante que cada jogo tenha 6 números únicos
        numero = randint(1, 60)  # Gera um número aleatório entre 1 e 60
        if numero not in numeros:  # Evita números repetidos
            numeros.append(numero)

    numeros.sort()  # Ordena os números do jogo
    lista.append(numeros[:])  # Adiciona uma cópia do jogo à lista de jogos
    numeros.clear()  # Limpa a lista para o próximo jogo

# Exibe os jogos gerados
print('-=' * 20)
print(f'{"JOGOS GERADOS":^40}')
print('-=' * 20)
for i, jogo in enumerate(lista, 1):
    print(f'Jogo {i}: {jogo}')
