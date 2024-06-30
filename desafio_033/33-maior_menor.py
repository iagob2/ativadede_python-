a = float(input('Informe o numero A: '))
b = float(input('Informe o numero B: '))
c = float(input('Informe o numero C: '))

menor = maior = a

if b < a and b < c :
    menor = b 
elif c < a and c < b:
    menor = c 

if b > a and b > c :
    maior = b
elif c > a and c > b :
    maior = c 
    
print(f'O menor numero é { menor} e o maior numero é {maior}')