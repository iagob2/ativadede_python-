def obter_numeros():
    numero_1 = float(input('Informe o primeiro número: '))
    numero_2 = float(input('Informe o segundo número: '))
    return numero_1, numero_2

n1, n2 = obter_numeros()

while True:
    print('\nEscolha uma opção:')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    op = int(input('Opção: '))

    if op == 1:
        print(f'A soma:\n {n1} + {n2} = {n1 + n2}')
    elif op == 2:
        print(f'A multiplicação:\n {n1} x {n2} = {n1 * n2}')
    elif op == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o {n2}')
        elif n2 > n1:
            print(f'O número {n2} é maior que o {n1}')
        else:
            print('Os números são iguais')
    elif op == 4:
        n1, n2 = obter_numeros()
    elif op == 5:
        print('Saindo do programa')
        break
    else:
        print('Opção inválida!!!')

print('Volte sempre!')
