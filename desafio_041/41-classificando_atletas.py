from datetime import date 

nasc = int(input('Infomer seu ano de nascimento : '))
ano = date.today().year
idade =   ano - nasc

print('Clássificação de atleta: ')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19 :
    print('Junior')
elif idade <= 25 :
    print('Sênior')
else:
    print('Master')
