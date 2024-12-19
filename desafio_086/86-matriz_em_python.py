# Inicializa a matriz como uma lista vazia
matriz = [[], [], []]

# Preenchendo a matriz com valores fornecidos pelo usuário
for l in range(3):  # Laço para as linhas
    for c in range(3):  # Laço para as colunas
        num = int(input(f'Digite um número para posição ({l},{c}): '))
        matriz[l].append(num)  # Adiciona o número na sublista correspondente

# Exibindo a matriz formatada
print('-=' * 30)
for linha in matriz:
    for valor in linha:
        print(f'{valor:^5}', end=' ')  # Formata o número com espaçamento centralizado
    print()  # Quebra de linha ao final de cada linha da matriz
