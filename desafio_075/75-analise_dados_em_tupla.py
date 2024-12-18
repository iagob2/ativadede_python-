# Solicita ao usuário que insira 5 números inteiros e os armazena em uma tupla
numeros = tuple(int(input('Digite um número: ')) for _ in range(5))

# Exibe todos os números digitados
print(f'Você digitou os valores: {numeros}')

# Conta quantas vezes o número 9 aparece na tupla
print(f'O valor 9 apareceu {numeros.count(9)} vezes')

# Verifica se o número 3 está presente na tupla e, se sim, exibe sua posição
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

# Exibe os números pares presentes na tupla
print('Os valores pares são: ', end='')
for n in numeros:
    if n % 2 == 0:  # Verifica se o número é par
        print(n, end=' ')
