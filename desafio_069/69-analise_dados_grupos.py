op = ' '  # Variável para controlar se o usuário deseja continuar
c = 1  # Contador de pessoas
h = mulherMenor20 = pMaio18 = 0  # Contadores para homens, mulheres menores de 20 e pessoas maiores de 18

while op not in 'N':
    # Solicita a idade e o sexo da pessoa
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Digite o sexo [M/F] da {c}ª pessoa: ')).strip().upper()[0]

    # Verifica se a pessoa tem 18 anos ou mais
    if idade >= 18:
        pMaio18 += 1

    # Verifica se a pessoa é homem
    if sexo == 'M':
        h += 1

    # Verifica se a pessoa é mulher e tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulherMenor20 += 1

    c += 1  # Incrementa o contador de pessoas
    # Pergunta se o usuário deseja continuar
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

# Exibe os resultados finais
print(f'Total de pessoas com mais de 18 anos: {pMaio18}')
print(f'Ao todo, temos {h} homem(ns) cadastrados.')
print(f'E temos {mulherMenor20} mulher(es) com menos de 20 anos.')
