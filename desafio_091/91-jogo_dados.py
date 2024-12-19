from random import randint

# Criação do dicionário de jogadores
jogadores = dict()

# Gerando valores aleatórios para cada jogador
for c in range(4):
    jogadores[f'jogador {c+1}'] = randint(1, 6)

# Exibindo os resultados dos jogadores
print("Resultados:")
for jogador, valor in jogadores.items():
    print(f"{jogador}: {valor}")

# Identificando o(s) vencedor(es)
maior_valor = max(jogadores.values())  # Maior valor obtido
vencedores = [jogador for jogador, valor in jogadores.items() if valor == maior_valor]  # Lista de vencedores

# Exibindo o resultado final
if len(vencedores) > 1:
    print(f"Houve um empate entre os jogadores {', '.join(vencedores)} com o valor {maior_valor}.")
else:
    print(f"O vencedor é {vencedores[0]} com o valor {maior_valor}.")



