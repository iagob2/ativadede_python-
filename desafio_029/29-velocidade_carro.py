vel = float(input("Informe a velocidade do veiculo:").strip())

if vel > 80 :
    mult = (vel - 80)* 7
    print(f'Você ultrapassor o limiter de velocidade sua multa é de {mult}')
else:
    print('Você não ultrapassor o limiter de velocidade ')