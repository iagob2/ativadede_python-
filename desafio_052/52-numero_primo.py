num = int(input('Informe qualquer numero para ver ser é primo:'))
tot = 0

for c in range(1,num+1):
    if num % c == 0 :
        print('\033[34m',end=' ')
        tot += 1
    else:
        print('\033[31m',end=' ')
    print(c, end=' ')
print(f'\n \033[mO número {num} foi divisivel {tot} vezes')
if tot == 2 :
    print('e por isso ele é primo!!!')
else:
    print('e por isso ele não é primo!!')