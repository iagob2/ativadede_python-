'''3. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Exemplo:
123 = 1 centena(s), 2 dezena(s) e 3 unidade(s)
12 = 1 dezena(s) e 2 unidade(s)'''


num = int(input('digite um numero inteiro menor que 1000: '))
while num > 1000:
    num = int(input('digite um numero inteiro menor que 1000: '))

u = num // 1%10
d = num // 10%10
c = num // 100%10

print('{} centena(s),{} dezena(s) e {} unidade(s)'.format(c,d,u))


