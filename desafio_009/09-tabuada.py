num = int(input('Digite um Numero para ver sua tabuada:'))

print('Tabuadado do ',num)

for n in range(0,11):
    print('{} X {} = {}'.format(num, n , num*n))