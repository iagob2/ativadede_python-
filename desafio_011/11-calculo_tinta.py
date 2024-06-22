# Solicita ao usuário a largura e a altura
l = float(input('Informe a largura (em metros): '))
a = float(input('Informe a altura (em metros): '))

# Calcula a área
area = l * a

# Calcula a quantidade de tinta necessária (considerando que 1 litro de tinta pinta 2 metros quadrados)
quant = area / 2

# Exibe os resultados 
print('\n--- Resultado ---\n')
print(f'A área a ser pintada é de {area:.2f} m²')
print(f'A quantidade de tinta necessária é de {quant:.2f} litros\n')
