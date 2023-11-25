'''2. Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor'''

reg = {'NomeFunc':'','salMes':float(1800),'comissão':float(),'carroVend': int(),'salTotal':float() }

reg['NomeFunc'] = input('digite o nome do funcionario:')
reg['carroVend'] = int(input('quantidade de carros vendido pelo funcionario:'))
reg['comissão'] = (reg['salMes']*5/100)*reg['carroVend']
reg['salTotal']= reg['salMes']+ reg['comissão']

for x,y in reg.items():
    print(x,y)