n = int(input('Informe um núemro qualquer inteiro:'))
print(' [1] -binário\n [2] -octal\n [3] -hexadeximal')
op = int(input('escola a opção: '))

if op == 1 :
    print(f'seu numero é {n} = {bin(n)} binário')

elif op == 2 :
    print(f'seu numero é {n} = {oct(n)} octal')
    
elif op == 3 : 
    print(f'seu numero é {n} = {hex(n)} hexadeximal')

    

