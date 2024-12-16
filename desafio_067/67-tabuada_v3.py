while True:
    # Solicita ao usuário um número para gerar a tabuada
    n = int(input("Digite um número para ver sua tabuada (número negativo encerra o programa): "))

    # Condição de parada: número negativo
    if n < 0:
        break
    else:
        print('-' * 30)
        print(f'Tabuada do {n}')  # Título da tabuada
        # Gera a tabuada de 1 a 10
        for c in range(1, 11):
            print(f'{n} x {c} = {n * c}')
        print('-' * 30)

# Mensagem final ao encerrar o programa
print('Programa de tabuada encerrado. Volte sempre!')
