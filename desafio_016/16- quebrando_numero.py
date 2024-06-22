import math 

# Solicita ao usuário um número qualquer
num = float(input('Informe um valor qualquer com ponto: '))

# Calcula a parte inteira do número usando math.trunc
parte_inteira = math.trunc(num)

# Exibe o número informado e sua parte inteira
print('\n--- Resultado ---')
print(f'O valor informado foi {num:.2f}.')
print(f'Sua parte inteira, calculada utilizando a função trunc da biblioteca math, é {parte_inteira}.\n')
