'''
Leia 2 notas, menor 5 (reprovado), media 5 e 6.9 Recuperação, maior ou igual 7 aprovado
'''
nota1 = float(input('Prova 1: '))
nota2 = float(input('Prova 2: '))
media = (nota1 + nota2)/2
if media < 5:
    print('Reprovado')
elif (media >= 5) and (media <= 6.9):
    print('Recuperação')
elif media > 7:
    print('Aprovado')
