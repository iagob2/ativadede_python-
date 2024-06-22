
print('\n--- aluguel de carros ---\n')

# Solicita ao usuário a quantidade de dias alugados e a quantidade de quilômetros rodados
dias = int(input('Quantos dias alugados? '))
kms = float(input('Quantos kms rodados? '))

# Calcula o valor total a pagar
pagar = (dias * 60) + (kms * 0.15)

# Calcula a média de quilômetros rodados por dia
media_kms_por_dia = kms / dias

# Exibe os resultados formatados com duas casas decimais
print('\n--- Resultado ---\n')
print(f'Valor total a pagar é de R$ {pagar:.2f}')
print(f'Média de kms rodados por dia: {media_kms_por_dia:.2f} km\n')
