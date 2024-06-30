frase = input('Digite um frase:').strip()
vezA = frase.lower().count('a')
primeiroA= frase.lower().find('a')
ultA = frase.lower().rfind('a')

print(f'a letra A aparece {vezA} vezes na frase. \n A primeira vez foi na posição {primeiroA}  e ultima ver foi na posição {ultA}')