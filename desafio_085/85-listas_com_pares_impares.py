# Criação de uma lista com duas sublistas: uma para pares e outra para ímpares
numeros = [[], []]

# Loop para entrada de 7 números
for c in range(7):
    n = int(input(f'Digite o número {c + 1}: '))
    if n % 2 == 0:
        numeros[0].append(n)  # Adiciona o número à sublista de pares
    else:
        numeros[1].append(n)  # Adiciona o número à sublista de ímpares

# Exibição dos resultados
print('-' * 40)
print(f'Números pares: {sorted(numeros[0])}')  # Exibe os pares em ordem crescente
print(f'Números ímpares: {sorted(numeros[1])}')  # Exibe os ímpares em ordem crescente
