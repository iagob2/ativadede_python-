num = int(input('Digite um Numero para ver sua tabuada:'))

print('Tabuadado do ',num)

c = 0
while c < 11:
    print('{} X {} = {}'.format(num, c , num*c))
    c += 1