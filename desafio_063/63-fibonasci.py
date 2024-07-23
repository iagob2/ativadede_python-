num = int(input('Quantos termos você quer mostrar da sequência de Fibonacci? '))

# Verificar se o número de termos é válido
if num <= 0:
    print("Por favor, insira um número maior que 0.")
else:
    # Mostrar os primeiros dois termos da sequência de Fibonacci
    t1, t2 = 0, 1
    print(t1, end=' -> ')
    
    if num > 1:
        print(t2, end=' -> ')
    
    # Gerar e mostrar os termos restantes da sequência de Fibonacci
    c = 3
    while c <= num:
        t3 = t1 + t2
        print(t3, end=' -> ')
        t1, t2 = t2, t3
        c += 1
    
    print('Fim')

    