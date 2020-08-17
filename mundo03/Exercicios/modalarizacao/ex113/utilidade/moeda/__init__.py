def metade(valor = 0, formato = False):
    valor /= 2
    return valor if  not formato else moeda(valor)

def dobro(valor = 0, formato = False):
    valor *= 2
    return valor if  not formato else moeda(valor)

def aumenta(valor = 0, aumenta = 0, formato=False):
    valor += (valor*aumenta)/100
    return valor if  not formato else moeda(valor)

def diminui(valor = 0, diminui = 0, formato = False):
    valor -= (valor*diminui)/100
    return valor if  not formato else moeda(valor)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')    

def resumo(valor=0, taxaa=10,  taxar=5):
    print('~'*30)
    print('RESUMO DO VALOR'.center(30))
    print('~'*30)
    print('Preço analizado: \t', moeda(valor))
    print('Dobro do Preço:\t\t', dobro(valor,True))
    print('Metade do Preco: \t', metade(valor,True))
    print('Aumento 10%: \t\t', aumenta(valor,taxaa,True))
    print('Redução 13%: \t\t', diminui(valor,taxar,True))
    print('-'*30)