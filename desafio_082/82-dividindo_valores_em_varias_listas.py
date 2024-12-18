# Inicializa listas vazias para armazenar os números, números pares e ímpares
numeros = []
par = []
impar = []

# Loop infinito para adicionar números à lista
while True:
    # Solicita ao usuário um número inteiro
    n = int(input('Digite um número: '))
    numeros.append(n)  # Adiciona o número à lista principal
    print('Número adicionado com sucesso!')
  
    # Pergunta ao usuário se deseja continuar
    r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':  # Sai do loop se a resposta for 'N'
        break

# Classifica os números da lista principal em pares e ímpares
for n in numeros:
    if n % 2 == 0:  # Verifica se o número é par
        par.append(n)
    else:  # Caso contrário, o número é ímpar
        impar.append(n)

# Exibe os resultados
print(f'\nA lista de números digitados: {numeros}')
print(f'A lista de números pares: {par}')
print(f'A lista de números ímpares: {impar}')
