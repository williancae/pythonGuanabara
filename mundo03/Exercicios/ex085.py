expressao = str(input('Digite a expressão: '))
print(expressao)
abrindo = expressao.count('(')
fechando = expressao.count(')')
if abrindo == fechando:
    print('Operação é Valida')
else:
    print('Operação invalida')

# Solução Guanabara

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expressão é valida')
else:
    print('Sua Expressão não é valida')