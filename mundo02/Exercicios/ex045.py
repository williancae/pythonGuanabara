'''
entre com altura e Peso e de com resultado IMC
IMC = peso/altura²
'''
peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Abaixo do Peso')
elif  18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('SobrePeso')
elif 30 <= imc <= 40:
    print('Obeso')
else:
    print('Obesidade mŕbida')