# Solicita ao usuário que digite uma frase, remove espaços em branco extras e converte para maiúsculas
frase = input('Digite uma frase qualquer: ').strip().upper()

# Divide a frase em palavras e as junta novamente sem espaços
palavras = frase.split()
junto = ''.join(palavras)

# Inverte a string usando slicing
inverso = junto[::-1]

# Verifica se a string invertida é igual à original
if inverso == junto:
    print(f'Temos um palíndromo!!! Normal: {junto} | Invertido: {inverso}')
else:
    print(f'Não temos um palíndromo. Normal: {junto} | Invertido: {inverso}')
