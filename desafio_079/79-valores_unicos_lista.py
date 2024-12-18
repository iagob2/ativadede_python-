# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop infinito para adicionar números à lista
while True:
    # Solicita ao usuário um número
    n = float(input('Digite um número: '))
    
    # Adiciona o número à lista apenas se ele ainda não estiver presente
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado! Não será adicionado.')
    
    # Pergunta ao usuário se deseja continuar
    r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':  # Sai do loop se a resposta for 'N'
        break

# Ordena a lista em ordem crescente
numeros.sort()

# Exibe os números da lista ordenados
print(f'Os números na lista são: {numeros}')
