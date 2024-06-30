num = input('Digite um número: ').strip()

list = ' '.join(num).split()
uni = list[3]
dez = list[2]
cent = list[1]
mil = list[0]


print(f'Unidade: {uni}  Dezenas: {dez}  Centena: {cent}  Milhar: {mil}')

