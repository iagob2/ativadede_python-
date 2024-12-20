# Função para calcular a área do terreno
def area(l, a):
    return l * a  # Calcula a área

# Solicita os valores de entrada
largura = float(input('Digite a largura do terreno (em metros): '))
comprimento = float(input('Digite o comprimento do terreno (em metros): '))

# Exibe o resultado
print(f'A área do terreno é {area(largura, comprimento):.2f} metros quadrados.')
