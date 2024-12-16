print('{:-^40}'.format(' Caixa Eletrônica '))

valor_seque = int(input('Digite o valor a ser sacado: '))
valor = valor_seque

nota50 = nota20 = nota10 = moeda1 = 0

while True:
    if valor >= 50:
        valor -= 50
        nota50 += 1
    elif valor >= 20:
        valor -= 20
        nota20 += 1
    elif valor >= 10:
        valor -= 10
        nota10 += 1
    elif valor >= 1:
        valor -= 1
        moeda1 += 1
    else:
        break

print(f'O valor solicitado foi R${valor_seque}, e as cédulas/moedas entregues foram:')

if nota50 != 0:
    print(f'{nota50} cédula(s) de R$50')
if nota20 != 0:
    print(f'{nota20} cédula(s) de R$20')
if nota10 != 0:
    print(f'{nota10} cédula(s) de R$10')
if moeda1 != 0:
    print(f'{moeda1} moeda(s) de R$1')
