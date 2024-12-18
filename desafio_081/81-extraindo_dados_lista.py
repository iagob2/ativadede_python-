# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop infinito para adicionar números à lista
while True:
    # Solicita ao usuário um número inteiro
    n = int(input('Digite um número: '))
    numeros.append(n)  # Adiciona o número à lista
    print('Número adicionado com sucesso!')
  
    # Pergunta ao usuário se deseja continuar
    r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':  # Sai do loop se a resposta for 'N'
        break

# Exibe a quantidade de números digitados e a lista completa
print(f'\nForam digitados {len(numeros)} números: {numeros}')

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)
print(f'A lista de números em ordem decrescente: {numeros}')

# Verifica se o número 5 está na lista
if 5 in numeros:
    print('Há pelo menos um número cinco na lista.')
else:
    print('Não há nenhum número cinco na lista.')
