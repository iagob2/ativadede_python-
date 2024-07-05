pesos = []
maior_peso = 0
menor_peso = 0

for n in range(5):
    peso = float(input(f'Informe o peso da {n+1}ª pessoa: '))
    
    # Inicializa o maior e o menor peso com o primeiro valor inserido
    if n == 0:
        maior_peso = menor_peso = peso
    else:
        # Verifica se o peso atual é maior que o maior peso registrado
        if peso > maior_peso:
            maior_peso = peso
        
        # Verifica se o peso atual é menor que o menor peso registrado
        if peso < menor_peso:
            menor_peso = peso
    
    pesos.append(peso)

# Exibe os pesos informados
print(f'Os pesos das pessoas são: {pesos}')

# Exibe o maior e o menor peso
print(f'O maior peso é {maior_peso}')
print(f'O menor peso é {menor_peso}')
