# '''Metodos de entrada e Saida'''
# # n1 = int(input('digite um numero: ')) #é nescessario dizer que tipo de valor voce recebe int(),float(),bool(),str()
# # n2 = int(input('Digite segundo numero: '))
# # s = n1 + n2
# # print('A some é ',s)
# # print('A soma vale {}'.format(s))
# # ==================
# Exemplo
# n1 = (input('digite um numero: '))
# n2 = int(input('Digite segundo numero: '))
# # s = n1 + n2
# # print('A some é ',s)
# # print('A soma vale {}'.format(s))
# print(n1.isnumeric()) #Verifica  se o numero é numerico se sim True se não False
# print(n1.isalpha()) #Apenas Letras
# print(n1.isalnum()) #letras e numeros
# print(n1.isupper()) #Verifica se é apenas maiuscula
#
# ============ Pratica ==============
# # numero 1
# a = int(input('1° numero: '))
# b = int(input('2° numero: '))
# soma = a + b
# print('A soma de {} e {} é  {}'.format(a,b,soma))

# # numero 2
# a = input('Digite um numero: ')
# print(a.isalnum()) #letras e numeros
# print(a.isupper()) #lestras todas em maiusculo
# print(a.isalpha()) #se contem apenas letras
# print(a.isnumeric()) #se contem apenas numero
# print(a.isdecimal()) #Verifica se é um numero de ponto flutuante
# print(a.isspace()) #verifica se é um espaço