from random import randint

# Função para sortear números aleatórios
def sortear(num):
    numeros = [randint(1, 100) for _ in range(num)]
    return numeros

# Função para somar apenas os números pares de uma lista
def somarPar(numeros):
    soma_pares = sum(n for n in numeros if n % 2 == 0)
    return soma_pares

# Sorteio de 5 números aleatórios
numeros = sortear(5)

# Exibe os números sorteados e a soma dos pares
print(f'Números sorteados: {numeros}')
print(f'Soma dos números pares: {somarPar(numeros)}')
