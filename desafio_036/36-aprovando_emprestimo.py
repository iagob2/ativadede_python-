vl_casa  = float(input('Informe o valor da casa que você quê comprar: '))
sl = float(input('Informe o salário do comprando: '))
quant_anos = int(input('Informoe quantas anos ele vai demorar para pagar: '))

prest = vl_casa / (quant_anos*12)
limiter = sl * 0.3

print(f'para pagar uma case de R${vl_casa} em {quant_anos} anos a prestação da casa séra de R${prest:.2f}')

if prest  > limiter:
    print('Empréstimo Negado!!!!')
else:
    print('Empréstimo pode ser concedido!')
    