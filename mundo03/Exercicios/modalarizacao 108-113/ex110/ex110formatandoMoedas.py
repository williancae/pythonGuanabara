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

