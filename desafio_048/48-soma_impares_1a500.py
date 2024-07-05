total = 0

for n in range(1,501):
    if n%2 == 1 and n%3 == 0 :
        total += n
print(f'A soma de todos os numero impres multiplos de três é {total}')
