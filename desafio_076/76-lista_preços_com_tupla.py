# Tupla contendo nomes de produtos e seus respectivos preços
produtos = (
    'Arroz', 20.50,
    'Feijão', 12.30,
    'Macarrão', 8.90,
    'Leite', 5.20,
    'Café', 15.00,
    'Açúcar', 4.80,
    'Óleo', 9.70,
    'Farinha', 6.50
)

# Exibindo os produtos e seus preços formatados
print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)

# Itera pela tupla, exibindo o nome e o preço de forma organizada
for i in range(0, len(produtos), 2):  # Percorre os índices pares (nomes dos produtos)
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:<30} R$ {preco:>7.2f}')

print('-' * 40)
