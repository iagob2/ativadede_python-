'''5. Faça um programa para ler 3 valores inteiros e escrevê-los em ordem decrescente.'''

num1 =int(input('digite um numero 1 inteiro:'))
num2 =int(input('digite um numero 2  inteiro:'))
num3 =int(input('digite um numero 3 inteiro:'))

m1 = m2 = m3 = num1

if num2 > m1 and num2 > num3:
    m1 = num2
elif num2 < m3 and num2 < num3:
    m3 = num2
else:
    m2 = num2

if num3 > m1 and num3 > num2:
    m1 = num3
elif num3 < m3 and num3 < num2:
    m3 = num3
else:
    m2 = num3



print('{} , {} , {}'.format(m1,m2,m3))