total = custamMais1000 = barato = 0
nomeMaisbarato = ' '
op = ' '  # Inicializa a variável de controle do loop

while op not in 'N':
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    total += preco  # Soma o preço ao total

    # Conta produtos que custam mais de R$1000
    if preco > 1000:
        custamMais1000 += 1

    # Verifica o produto mais barato
    if barato == 0 or preco < barato:
        barato = preco
        nomeMaisbarato = nome

    # Pergunta se o usuário deseja continuar
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

# Exibe os resultados
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {custamMais1000} produto(s) custando mais de R$1000.')
print(f'O produto mais barato foi "{nomeMaisbarato}" que custa R${barato:.2f}')
