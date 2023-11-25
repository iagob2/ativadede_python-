'''4. Faça um Programa que leia os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Se sim, calcule e mostre a área do triângulo.'''

a = float(input('digite o valor do lado A:'))
b = float(input('digite o valor do lado B:'))
c = float(input('digite o valor do lado C:'))

s = float((a+b+c)/2)
f = float( s*(s-a)*(s-b)*(s-c))
area =float(f**(1/2)) 


if(a+b > c ) and (a + c > b) and (b+c > a ):
    print("a soma dos lado da um triângulo, e sua area é de {:.2f}".format(area))

else:
    print("a soma dos lado não da um triângulo")