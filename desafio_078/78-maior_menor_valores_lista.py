# Cria uma lista com 5 valores digitados pelo usuário
valores = list(int(input('Digite um valor: ')) for _ in range(5))

# Exibe todos os valores digitados
print(f'Os valores digitados são: {valores}')

# Determina o maior valor e sua posição na lista
maior_valor = max(valores)
posicao_maior = valores.index(maior_valor)
print(f'O maior valor é {maior_valor} e ele está na posição {posicao_maior}')

# Determina o menor valor e sua posição na lista
menor_valor = min(valores)
posicao_menor = valores.index(menor_valor)
print(f'O menor valor é {menor_valor} e ele está na posição {posicao_menor}')
