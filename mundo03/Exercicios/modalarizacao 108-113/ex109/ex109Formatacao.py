def metade(valor = 0):
    valor /= 2
    return valor

def dobro(valor = 0):
    valor *= 2
    return valor

def aumenta(valor = 0, aumenta = 0):
    valor += (valor*aumenta)/100
    return valor

def diminui(valor = 0, diminui = 0):
    valor -= (valor*diminui)/100
    return valor

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')    