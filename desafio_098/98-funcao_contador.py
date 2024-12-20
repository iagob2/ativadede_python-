# Função para contar de um número inicial até um final, com um passo definido
def contador(inicio, fim, passo):
    # Garante que o passo não seja zero
    if passo == 0:
        passo = 1

    # Ajusta o passo para contagem decrescente, se necessário
    if inicio > fim and passo > 0:
        passo = -passo

    # Realiza a contagem
    for c in range(inicio, fim, passo):
        print(c, end=' -> ')
    print('Fim!')  # Indica o fim da contagem

# Testes da função com diferentes parâmetros
contador(1, 11, 1)   # Contagem crescente de 1 a 10
contador(10, 0, -2)  # Contagem decrescente de 10 a 1 com passo -2

print('-='*20)
print('agora é sua vez de personalizar a contagem!!')
ini = int(input('inicio:'))
fim = int(input('Fim:'))
pas = int(input('passo:'))
contador(ini,fim,pas)