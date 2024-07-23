# primeiro = int (input('Informe o primeiro termo: '))
# razao = int(input('Informe a razão: '))
# decimo = primeiro + (10-1)*razao

# while primeiro < decimo :
#     print(primeiro , end=' -> ')
#     primeiro += razao
# print('acabou')

#melhorando
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
termo_atual = primeiro_termo

while (razao > 0 and termo_atual <= decimo_termo) or (razao < 0 and termo_atual >= decimo_termo):
    print(termo_atual, end=' -> ')
    termo_atual += razao

print('acabou')
