# Tupla contendo os números por extenso de 0 a 20
numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
    'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 
    'dezessete', 'dezoito', 'dezenove', 'vinte'
)

# Variável para controlar a repetição do programa
resp = ' '

while resp not in 'N':  # Loop principal para continuar ou encerrar o programa
    while True:  # Loop interno para validar o número digitado
        # Solicita ao usuário um número entre 0 e 20
        num = int(input('Digite um número inteiro de 0 a 20: '))
        
        # Verifica se o número está dentro do intervalo permitido
        if 0 <= num <= 20:
            break  # Sai do loop interno se o número for válido
        
        # Mensagem de erro para números fora do intervalo
        print('Número inválido. Tente novamente.')
    
    # Exibe o número por extenso correspondente
    print(f'Você digitou o número {numeros[num]}')
    
    # Pergunta ao usuário se deseja continuar
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

# Mensagem final ao encerrar o programa
print('Programa encerrado. Obrigado por usar!')
