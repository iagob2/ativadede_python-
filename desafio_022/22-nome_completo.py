nome_completo = input("Informe seu nome completo: ")

print(f' O seu nome é {nome_completo}')
print(f' Em Maiúscula é {nome_completo.upper()} \n Em Minúsculo é {nome_completo.lower()}  ') 
print(f' Seu nome tem ao todo {len(nome_completo) - nome_completo.count(' ')} letras')
primeiro = nome_completo.split()
print(f' Seu primeiro nome é {primeiro[0]} e ele tem { len(primeiro[0])} letras')