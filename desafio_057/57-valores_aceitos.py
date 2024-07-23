s = input('Informe seu sexo:[M/f] ').strip().upper()[0]
while s not in 'MF':
    s = input('dados inválidos. Por favor Informe seu sexo:[M/f] ').strip().upper()[0]
    
print(f'Sexo {s} registrado com sucesso ')
