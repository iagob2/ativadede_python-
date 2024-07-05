from random import randint
from time import sleep 

print('Game de Jokenpô:')

itens = ['pedra', 'papel', 'tesoura']
pc = randint(0, 2)

op = int(input('Escolha sua opção\n[0] Pedra\n[1] Papel\n[2] Tesoura\nop: '))

print('Processando...')
sleep(1)

if op == pc:
    print(f'Empate!!! Eu joguei {itens[pc]} e você também jogou {itens[op]}.')
elif op == 0 and pc == 1:
    print(f'Você perdeu, eu ganhei!!! Eu joguei {itens[pc]} e você jogou {itens[op]}.')
elif op == 0 and pc == 2:
    print(f'Você ganhou, eu perdi!!! Eu joguei {itens[pc]} e você jogou {itens[op]}.')
elif op == 1 and pc == 0:
    print(f'Você ganhou, eu perdi!!! Eu joguei {itens[pc]} e você jogou {itens[op]}.')
elif op == 1 and pc == 2:
    print(f'Você perdeu, eu ganhei!!! Eu joguei {itens[pc]} e você jogou {itens[op]}.')
elif op == 2 and pc == 0:
    print(f'Você perdeu, eu ganhei!!! Eu joguei {itens[pc]} e você jogou {itens[op]}.')
elif op == 2 and pc == 1:
    print(f'Você ganhou, eu perdi!!! Eu joguei {itens[pc]} e você jogou {itens[op]}.')
else:
    print('Opção inválida!!! Parando o jogo.')
