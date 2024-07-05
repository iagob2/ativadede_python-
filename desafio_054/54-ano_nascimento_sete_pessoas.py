from datetime import date

# Inicializa as variáveis
idades = []
somar_maiores_idade = 0
somar_menores_idade = 0

# Laço para coletar dados de 7 pessoas
for n in range(7):
    nasc = int(input(f'Informe seu ano de nascimento da {n+1}ª pessoa: '))
    ano = date.today().year
    idade = ano - nasc
    
    # Verifica se a pessoa é maior ou menor de idade
    if idade >= 21:
        somar_maiores_idade += 1
    else:
        somar_menores_idade += 1
    
    # Adiciona a idade à lista de idades
    idades.append(idade)

# Exibe o resultado
print(f'a idade das pessoas {idades}')
print(f'{somar_maiores_idade} pessoas são maiores de idade.')
print(f'{somar_menores_idade} pessoas são menores de idade.')
