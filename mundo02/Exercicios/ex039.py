'''
Transformar numero inteiro pra octal, hexa e binario
'''
import math
num = int(input('Digite um numero: '))
op = int(input('Transformar numero para:\n[1] Binario\n[2] Hexadecimal\n[3] Octal\nDigite sua opção: '))
if op == 1:
    num = bin(num)
    print("Convertido Para Binario: {}".format(num))
elif op == 2: 
    num = hex(num)
    print("Coonvertido para Hexadecimal: {}".format(num))
elif op == 3:
    num = oct(num)
    print('Conertido para  Octal: {}'.format(num))
