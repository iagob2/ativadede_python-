import math 

print('\n--- Cálculo da Hipotenusa ---\n')

# Solicita ao usuário o comprimento dos catetos
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

# Calcula a hipotenusa usando math.hypot
hi = math.hypot(co, ca)

# Exibe o resultado 10

print(f'\nPara cateto oposto de {co:.2f} e cateto adjacente de {ca:.2f}, a hipotenusa mede {hi:.2f}\n')
