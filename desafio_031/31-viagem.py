dis = float(input('Informe a distância da sua viagem em km: '))

if dis < 200:
    print(f'o custo da viagem e de R${dis*0.50}')
else:
    print(f'o custo da viagem e de R${dis*0.45}')
