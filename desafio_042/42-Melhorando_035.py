r1 = float(input('Primeiro segmentos: '))
r2 = float(input('Segundo segmentos: '))
r3 = float(input('Terciro segmentos: '))

if r1 < r2 + r3  and r2 < r1 + r3  and r3 < r2 + r1:
    if r1 == r2 and r2 == r3 and r1 == r3:
        tipo = 'Equilátero'
    elif r1 == r2 or r2 == r3 or r1 == r3:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
        
    print(f'Os segmentos acima podem fromar um Triângulo!! do tipo {tipo} ')
    
else:
    print('Os segmentos acima não podem formar triângulo!')