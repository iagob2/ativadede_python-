salario = float(input('Informe seu salario: '))

if salario > 1250:
    aum = salario * 0.1
    print(f'O seu salario é de R${salario} e o aumento dele é de {aum} , no total ficar R${salario + aum}')
else:
    aum = salario * 0.15
    print(f'O seu salario é de R${salario} e o aumento dele é de {aum} , no total ficar R${salario + aum}')