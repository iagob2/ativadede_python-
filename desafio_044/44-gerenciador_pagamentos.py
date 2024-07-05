val = float(input("Informe quanto custa o produto: "))
print('Formas de pagamento:')
print('[1] à vista dinheiro/cheque\n[2] no cartão:')
op1 = int(input('Opção: '))

if op1 == 1:
    desc = val * 0.10
    print(f'Sua compra de R${val:.2f} terá um desconto de 10%, custando R${val - desc:.2f}.')
else:
    par = int(input('Informe quantas vezes deseja parcelar: '))
    if par == 1 or par == 0:
        desc = val * 0.05
        print(f'Sua compra de R${val:.2f} terá um desconto de 5%, custando R${val - desc:.2f}.')
    elif par == 2:
        print(f'Cada parcela da compra de R${val:.2f} será de R${val / 2:.2f} sem juros.')
    else:
        juros = val * 0.20
        print(f'Cada parcela da compra de R${val:.2f} será de R${(val + juros) / par:.2f} com 20% de juros.')
