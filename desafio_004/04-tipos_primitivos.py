v = input('Digite algo: ')

print('O tipo primitivo desse valor {} é {}'.format(v, type(v)))
print('Só tem espaços ??? ', v.isspace())
print('É um numero ???',v.isnumeric())
print('É alfabéfico ???',v.isalpha())
print('É alfanumérico ???',v.isalnum())
print('Está em maiúsculas ???',v.isupper())
print('Está em minúsculas ???',v.islower())
print('Está capitalizada ???',v.istitle())
