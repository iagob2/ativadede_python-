from datetime import date 

nasc = int(input('Infomer seu ano de nascimento : '))
ano = date.today().year
idade =   ano - nasc

if idade < 18:
    print(f'você tem {idade} anos , ainda falta { 18 - idade } anos para se alistar')
elif idade > 18 :
    print(f'você tem {idade} anos ,  já passou {idade - 18 } depois do seu alistamento')
else:
    print(f'você tem {idade} anos , é hora de se alistar')


