# Inicializa a matriz como uma lista de listas vazias
matriz = [[], [], []]

# Variáveis para cálculos
somaPares = 0  # Soma dos números pares
somaTerceiraColuna = 0  # Soma dos valores da terceira coluna

# Preenchendo a matriz com valores fornecidos pelo usuário
for l in range(3):  # Laço para as linhas
    for c in range(3):  # Laço para as colunas
        num = int(input(f'Digite um número para posição ({l},{c}): '))
        matriz[l].append(num)  # Adiciona o número na sublista correspondente

# Exibindo a matriz formatada e realizando os cálculos
print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'{matriz[l][c]:^5}', end=' ')  # Exibe o número centralizado
        if matriz[l][c] % 2 == 0:  # Verifica se o número é par
            somaPares += matriz[l][c]
        if c == 2:  # Verifica se está na terceira coluna
            somaTerceiraColuna += matriz[l][c]
    print()  # Quebra de linha ao final de cada linha da matriz

# Determina o maior valor da segunda linha
maiorSegundaLinha = max(matriz[1])

# Exibindo os resultados dos cálculos
print('-=' * 30)
print(f'A soma dos valores pares é: {somaPares}')
print(f'A soma dos valores da terceira coluna é: {somaTerceiraColuna}')
print(f'O maior valor da segunda linha é: {maiorSegundaLinha}')
