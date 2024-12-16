somar = c = 0  # Inicializa as variáveis para a soma e o contador

while True:
    n = int(input('Digite qualquer valor (999 para parar): '))  # Solicita ao usuário um número
    if n == 999:  # Verifica se o usuário deseja encerrar o programa
        break  # Encerra o loop
    else:
        somar += n  # Adiciona o número digitado à soma
        c += 1  # Incrementa o contador de números digitados

# Exibe o total de números digitados e a soma deles
print("Você digitou {} números e a soma deles é {}".format(c, somar))
