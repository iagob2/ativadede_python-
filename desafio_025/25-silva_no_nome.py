nome = input('Informe seu nome: ').strip()
resp = nome.lower().find('silva')

if resp > 0 :
    print(f'O seu nome é {nome} e ele tem silva nele')
else:
    print(f'O seu nome é {nome} e ele não  tem silva nele')

# resposta do professor:
# print('seu nome tem silva?{}'.format('silva' in nome.lower()))