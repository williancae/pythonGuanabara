def row(): #função de mostrar linha
    print('°°'*20)
def titulo(msg):
    print('°'*len(msg)) #tamanho da linha se adequa com numero da mensagem
    print(f'{msg}')
    print('°'*len(msg))
def soma(num1, num2):
    print(num1+num2)
def contador(*num):
    soma = 0
    for valor in num:
        soma += valor
    print(f'A soma de todos os numeros é {soma}')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'{lst}')


valores = [7,5,2,3,4]
dobra(valores)
contador(1,2,3,4)
row()
titulo('Alunos')
row()
num1 = int(input('num1 = '))
num2 = int(input('num2 = '))
soma(num1, num2)