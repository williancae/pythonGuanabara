'''
 Aprovar emprestimo bancario entradas valor casa,salario, quantos anos pra pagar---> condição prestaçã
'''
valorCasa = float(input('Valor da casa: '))
salario = float(input('Salario do cliente: '))
tempoPagamento = int(input('Em quantos anos ira pagar: '))

numPrestacoes = tempoPagamento * 12
precoPrestacoes = valorCasa / numPrestacoes
exceder = salario = ((salario*30)/100)
print(numPrestacoes,precoPrestacoes,exceder)
if precoPrestacoes > exceder:
    print('\33[:30mAs Prestações precisão ser menores a 30, emprestiomo \33[1:31mNegado!\33[m')
else:
    print('\33[:30mVocê tera que pagar {} parcelas durante os {} anos definidos.\n'
          'Cada parcela custara {:.2f}'.format(numPrestacoes, tempoPagamento, precoPrestacoes))
