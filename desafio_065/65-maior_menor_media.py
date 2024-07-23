resp = 'S'
soma = quant = 0
maior = menor = None

while resp in 'Ss':
    while True:
        try:
            num = float(input('Digite um número: '))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
    soma += num
    quant += 1
    
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    while True:
        resp = input('Quer continuar? [S/N]: ').upper().strip()
        if resp in 'SN':
            break
        else:
            print("Entrada inválida. Por favor, responda com 'S' ou 'N'.")

media = soma / quant
print(f'Você digitou {quant} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
