cid = input('Informe um nome de cidade: ').strip()
resp = cid[:5].upper() == 'SANTO'

if resp:
    print(f'O nome da cidade {cid} começar com  SANTO')
else : 
    print(f'O nome da cidade {cid} não começar com  SANTO')