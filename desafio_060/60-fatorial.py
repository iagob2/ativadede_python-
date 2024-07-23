num = int(input("Digite um numero para ver seu fatorial: "))
f = 1

print(f'Calculando {num}! ',end=' ')

for n in range(num,0,-1):
    if n == 1 :
         print(n,end=' = ') 
    else:
        print(n,end=' x ') 
    f *= n
    
print(f)

