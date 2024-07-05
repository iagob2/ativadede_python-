soma = 0
for n in range(1, 7):
    num = int(input(f'Informe o {n}º valor: '))
    if num % 2 == 0:
        soma += num

print(f'A soma dos valores pares foi {soma}')
