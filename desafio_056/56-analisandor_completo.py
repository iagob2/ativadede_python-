from datetime import date

somar_idade = 0 
somar_mulheres_menos_vinte = 0 
mais_velhor = 0
home_mais_velhor = ''

for p in range(1, 5):
    print(f'------Dados da {p}ª pessoa :')
    nome = input('Informe o nome: ').upper().strip()
    nasc = int(input('Informe o ano de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    somar_idade += idade
    sexo = input('Informe seu sexo: [M/F] ').upper().strip()
    
    if idade > mais_velhor and sexo == 'M':
        mais_velhor = idade
        home_mais_velhor = nome
    if idade < 20 and sexo == 'F':
        somar_mulheres_menos_vinte += 1

print(f'A média de idade do grupo é {(somar_idade / 4):.2f}')
print(f'O nome do homem mais velho é {home_mais_velhor} e ele tem {mais_velhor} anos')
print(f'No total, há {somar_mulheres_menos_vinte} mulheres com menos de vinte anos')
