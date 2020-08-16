# help(input) #ajuda com comando, biblioteca, funções e etc
# print(input.__doc__) ##ajuda com comando, biblioteca, funções e etc
# def sorteia(lista):
#     """[lista]
#     Args:
#         lista (list): [recebe valores aleatorios]
#     """
#     print('Numeros sorteados: ', end=' ')
#     for cont in range(0, 5):
#         n = randint(1, 10)
#         lista.append(n)
#         print(f'{n}', end=' ', flush=True)
#         sleep(0.3)
#     print('>>Pronto!!')
# help(sorteia) #Mostra os docstring da função

def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f*=c
    return f #retorna um valor pro codigo principal
f1 = fatorial(5)
print(f1) #printando o retorno
