primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo_termo = primeiro_termo + 9 * razao
termo_atual = primeiro_termo
mais = 1

while mais != 0:
    while (razao > 0 and termo_atual <= decimo_termo) or (razao < 0 and termo_atual >= decimo_termo):
        print(termo_atual, end=' -> ')
        termo_atual += razao
    
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    decimo_termo += mais * razao

print('Acabou')
