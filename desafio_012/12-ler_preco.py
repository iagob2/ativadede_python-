# Solicita ao usuário o preço do produto
preco = float(input('Informe o preço do produto: R$ '))

# Calcula o novo preço com um desconto de 5%
novo_preco = preco - (preco * 0.05)

# Exibe o novo preço 
print('\n--- Resultado   ---\n')
print(f'Novo preço como 5%  desconto: R$ {novo_preco:.2f}\n')
