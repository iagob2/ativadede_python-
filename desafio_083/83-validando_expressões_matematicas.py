# Solicita ao usuário uma expressão matemática
expressao = input('Digite a expressão: ')
pilha = []  # Inicializa uma pilha para verificar os parênteses

# Percorre cada caractere da expressão
for simbolo in expressao:
    if simbolo == '(':  # Se encontrar um parêntese de abertura
        pilha.append('(')  # Adiciona à pilha
    elif simbolo == ')':  # Se encontrar um parêntese de fechamento
        if pilha:  # Verifica se a pilha não está vazia
            pilha.pop()  # Remove o último parêntese de abertura
        else:  # Caso contrário, adiciona ')' à pilha e interrompe o loop
            pilha.append(')')
            break

# Verifica se a pilha está vazia, indicando que a expressão é válida
if not pilha:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
