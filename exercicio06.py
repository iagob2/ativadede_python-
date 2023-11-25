'''Faça um programa que leia um número indeterminado de valores correspondentes a notas de alunos e armazene-os em uma coleção Python. 

A entrada de dados encerra quando for digitado um valor menor que zero ou maior que 10 (que não deve ser armazenado). 

Encerre a entrada de dados com uma mensagem, em seguida, faça:
Exiba todos os valores;
Mostre a quantidade de valores que foram lidos;
Exiba o maior e o menor valor;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Altere todas as notas 5 para 6;
Mostre todos os valores após as modificações.'''

num= float(input('digite as nota do aluno:(se o valor for menor que zero ou maior que 10 o progama é encerrado:)'))
notas = []
while num >= 0 and num <= 10 :
    notas.append(num)
    
    num= float(input('digite as nota do aluno:(se o valor for menor que zero ou maior que 10 o progama é encerrado:)'))

print("foram lidos {} valores".format(len(notas)))

print("o maior valor é {} e o menor valor {} ". format(max(notas),min(notas)))

media = sum(notas)/len(notas)
print(" a media das notas é {:.2f}".format(media))

for x in notas:
    if x > media:
        print("os numero maiores que a media é:",x)
   
c = 0
while c < len(notas):
    if notas[c] == 5 :
        notas[c] = 6.0
    c += 1
print("alterando todas as notas 5 para 6;")
for x in notas:
    print(x)