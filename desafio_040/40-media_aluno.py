nota1 = float(input('Informe a nota da prova 1 : '))
nota2 = float(input('Informe a nota da prova 2 : '))
nota3 = float(input('Informe a nota da prova 3 : '))

media = (nota1 + nota2 + nota3)/3

if media < 5 :
    print(f'Média {media:.2f} , Reprovado')
elif media >= 5 and media < 7 :
    print(f'Média {media:.2f} , Recuperação')
elif media >= 7 :
    print(f'Média {media:.2f} , Aprovado ')

    