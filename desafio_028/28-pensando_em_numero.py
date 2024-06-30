import random 

print('Estou pensando em um número de 1 a 5, tenter ativinha:')
x = random.randint(1,5)

num = int(input('Informe o numero: '))

if num == x :
    print(f'você acertou!!! estava pensado no numero {x}')
else:
    print(f'você errou!!! estava pensado no numero {x}')
