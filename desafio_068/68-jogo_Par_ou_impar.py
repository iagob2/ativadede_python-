from random import randint

v = 0  # Contador de vitórias consecutivas

while True:
    print('Vamos jogar Par ou Ímpar!')

    # Solicita ao jogador que escolha entre Par ou Ímpar
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Digite sua opção (Par ou Ímpar): ')).strip().upper()[0]

    # Jogador escolhe um número
    jogador = int(input('Diga um valor: '))
    pc = randint(0, 10)  # Computador escolhe um número aleatório
    total = pc + jogador  # Soma dos números

    # Exibe os valores jogados e o resultado
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}.')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR!')
    print('-' * 30)

    # Verifica quem venceu
    if tipo == 'P':  # Jogador escolheu PAR
        if total % 2 == 0:
            print('Você venceu!!!')
            v += 1  # Incrementa o contador de vitórias
        else:
            print('Você perdeu!!!')
            break
    elif tipo == 'I':  # Jogador escolheu ÍMPAR
        if total % 2 == 1:
            print('Você venceu!!!')
            v += 1  # Incrementa o contador de vitórias
        else:
            print('Você perdeu!!!')
            break

    print('Vamos jogar novamente...')
    print('-' * 30)

# Exibe o total de vitórias ao final
print(f'GAME OVER! Você venceu {v} vez(es).')
