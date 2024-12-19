from datetime import datetime 

# Criação do dicionário para armazenar os dados
dados = dict()
dados['nome'] = str(input('Digite o seu Nome: '))
nasc = int(input('Digite o ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))

# Verifica se a CTPS é diferente de 0 para solicitar mais informações
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário (R$): '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

# Exibe os dados formatados
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
