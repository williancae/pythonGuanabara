aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'O aluno é {aluno["nome"]}\nMédia = {aluno["media"]}\nSituação {aluno["situacao"]}')
