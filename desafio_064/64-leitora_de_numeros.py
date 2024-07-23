cont = soma = 0

while True:
    num = int(input('Informe um valor (digite [999] para parar): '))
    if num == 999:
        print('Saindo do programa...')
        break
    else:
        cont += 1
        soma += num

print(f'Foram informados {cont} valores. O valor total deles é {soma}.')
