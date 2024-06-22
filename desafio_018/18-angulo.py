from math import radians,sin,cos,tan

ang = float(input('\nInforme um ângulo qualquer (em graus): '))
ang_rad = radians(ang)  # Converte o ângulo de graus para radianos


# Calcula os valores
seno = sin(ang_rad)
coss = cos(ang_rad)
tang = tan(ang_rad)


# Exibe os resultados 
print(f'\n--- Resultado para o ângulo de {ang:.2f} graus: ---\n')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {coss:.2f}')
print(f'Tangente: {tang:.2f}\n')


