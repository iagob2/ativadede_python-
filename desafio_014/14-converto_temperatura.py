# Solicita ao usuário o valor da temperatura em Celsius
c = float(input('Informe o valor da temperatura em Celsius: '))

# Converte a temperatura para Fahrenheit
f = c * 1.8 + 32

# Exibe o valor da temperatura em Fahrenheit 
print('\n--- Resultado ---\n')
print(f'O valor da temperatura em Fahrenheit é {f:.2f}°F\n')
