# Solicita ao usuário o valor do sálario 
valor = float(input('Informe o valor do sálário : R$ '))

# Calcula o novo salario com um aumento de 15%
novo_valor = valor + (valor * 0.15)

# Exibe o novo salario
print('\n--- Resultado   ---\n')
print(f'Novo sálário como 15%  de aumento: R$ {novo_valor:.2f}\n')
