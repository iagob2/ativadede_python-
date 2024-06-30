r1 = float(input('Primeiro segmentos: '))
r2 = float(input('Segundo segmentos: '))
r3 = float(input('Terciro segmentos: '))

if r1 < r2 + r3  and r2 < r1 + r3  and r3 < r2 + r1:
    print('Os segmentos acima podem fromar um Triângulo!!')
else:
    print('Os segmentos acima não podem formar triângulo!')