# Tupla com várias palavras sem acentos
palavras = (
    'livro', 'caderno', 'caneta', 'papel', 'computador', 
    'telefone', 'mesa', 'cadeira', 'janela', 'porta', 
    'carro', 'bicicleta', 'aviao', 'navio', 'hotel', 
    'restaurante', 'escola', 'universidade', 'professor', 'aluno'
)

# Exibindo as palavras da tupla
print('-' * 40)
print(f'{"Palavras na tupla:":^40}')
print('-' * 40)
for palavra in palavras:
    vogais = []  # Lista para armazenar as vogais
    for letra in palavra:
        if letra.lower() in 'aeiou':  # Verifica se a letra é uma vogal
            vogais.append(letra)  # Adiciona a vogal na lista
    print(f'Palavra: {palavra:<30} Vogais: {", ".join(vogais):>2}')  # Exibe as vogais encontradas
