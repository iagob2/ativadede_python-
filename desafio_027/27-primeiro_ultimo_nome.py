nome = input('Informe seu nome completo: ').strip()
list = nome.split()

print(f' o primeiro nome é { list[0]} e o ultimo nome é {list[len(list)-1]}')
