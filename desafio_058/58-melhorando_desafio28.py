import random 

print('Estou pensando em um número de 0 a 10, tente adivinhar:')
x = random.randint(0, 10)
tentativas = 0

while True:
    num = int(input('Informe o número: '))
    tentativas += 1

    if num == x:
        print(f'Você acertou!!! Eu estava pensando no número {x}.')
        break
    else:
        print('Você errou!!! Tente novamente.')

print(f'Você precisou de {tentativas} tentativas para acertar.')
