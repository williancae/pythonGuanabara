from time import sleep
def fatorial(num, show=False):
    """[fatorial]
    Args:
        num ([int]): [Numero no qual sera feito o fatoral]
        show (bool, optional): [Caso seja defino show=True, sera mostrado a operação do fatorial]. Defaults to False.
    """
    f = 1
    for m in range(num, 0, -1):
        if show:
            print(f'{m}', end=''), sleep(0.3)
            if m > 1: print(' x ', end='', flush=True), sleep(0.5)
            else: print(' = ', end='', flush=True), sleep(0.5)
        f *= m
    print(f)
# help(fatorial)
fatorial(int(input('Qual numero deseja tirar o fatorial?: ')), str(input('Deseja deseja ver aoperação escreva True, deixe em branco se nao: ')))