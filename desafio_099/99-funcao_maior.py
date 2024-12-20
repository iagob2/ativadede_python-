from random import randint


# Função para encontrar o maior número em uma lista
def maior(numeros):
    # Inicializa o maior número como o primeiro elemento da lista
    maior = numeros[0]
    
    # Percorre a lista para encontrar o maior número
    for n in numeros:
        if n > maior:
            maior = n
    return maior

# Lista de números para teste
numeros = [randint(1,1000) for _ in range(10)]

# Exibe a lista e o maior valor encontrado
print(f'Números: {numeros}')
print(f'O maior valor é {maior(numeros)}')
