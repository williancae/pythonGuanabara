from datetime import date
dataAtual = date.today()
anoAtual = dataAtual.year
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nascimento =  int(input('Ano de nascimento: '))
pessoa['idade'] = anoAtual - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if pessoa['ctps'] > 0:
    pessoa['contrato'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salario R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + 35
print('::'*40)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem valor de {v}')