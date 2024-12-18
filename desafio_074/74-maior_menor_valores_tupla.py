from random import randint

# Gerando os números aleatórios e armazenando-os diretamente em uma tupla
numeros = tuple(randint(1, 100) for _ in range(20))  # Gera 20 números aleatórios de 1 a 100

# Exibindo os números sorteados
print('Números sorteados:')
for n in numeros:
    print(f'{n}', end=' ')

# Exibindo o maior e o menor número sorteado
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
