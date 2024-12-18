lista = [ ]
for c in range(0,5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > lista[-1] :
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        p = 0 
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p,n)
                print(f'adiconado na posiçã {p} da lista..')
                break
            p += 1 
                
print('-='*30)
print(f'os valores digitados em ordem foram {lista}')