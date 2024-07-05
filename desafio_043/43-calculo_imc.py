peso = float(input('Informe o seu peso : '))
alt = float(input('Informe sua altura :'))

imc = peso / (alt**2) 

print('Calculondo o IMC:')
if imc < 18.5 :
    print('abaixo do peso ')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30 :
    print('sobrepeso')
elif imc >= 30 and imc < 40 :
    print('obesidade')
else:
    print('Obesidade mórbia')