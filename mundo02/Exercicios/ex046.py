'''
elabore um  programa que calcule o valor a ser pago  por um produto considerando o seu
PREÇO NORMAL  e CONDIÇÃO DE PAGAMENTO
'''
preco = float(input('Qual o preço do prduto: '))

cond = 0
while cond == 0:
    print('=== Opções de Pagamentos ===\n'
          '[1] - Dinheiro ou Cheque\n'
          '[2] - A vista no cartão\n'
          '[3] - 2x Cartão no cartão\n'
          '[4] - 3x ou mais no cartão\n')
    cond = int(input('Escolhas uma das formas de pagamento: '))
    if cond == 1:
        precoDesconto = preco - (preco * 10) /100
        print('Com desconto de 10% sobre o valor R$ {:.2f}, o preço final sera R$ {:.2f}.'.format(preco,precoDesconto))
    elif cond == 2:
        precoDesconto = preco - (preco*5)/100
        print('Com desconto de 5% sobre o valor R$ {:.2f}, o preço final sera R$ {:.2f}.'.format(preco, precoDesconto))
    elif cond == 3:
        print('Pagando em 2x no cartão nao sera cobrado taxa de juros preço final R$ {:.2f}'.format(preco))
    elif cond == 4:
        quantParcelas = int(input('Em quantas vezes voce ira dividir: '))
        precoJuros = (preco/quantParcelas)
        # print(precoJuros)
        precoParcelas = precoJuros + (precoJuros*20)/100 #Preco de cada parcela
        # print(precoParcelas)
        precoJuros = ((precoJuros*20)/100)*quantParcelas #juros sobre o numero de parcelas
        # print(precoJuros)
        precoFinal = preco + precoJuros
        print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(quantParcelas,precoParcelas))
        print('Sua compra de R${} vai custar R${} no final'.format(preco,precoFinal))
    else:
        print('\n\n==== ERRO! digite uma opção valida. ====')
        cond = 0