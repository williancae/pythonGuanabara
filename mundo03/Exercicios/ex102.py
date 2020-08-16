from datetime import date
ano = date.today()
def votacao(idade):
    if idade < 18 and idade >= 17:
        return 'Opcional'
    elif 18 <= idade <= 60:
        return 'Obrigatorio'
    else:
        return 'opcional'
anoNascimento = int(input('Quando nasceu: '))
idade = ano.year - anoNascimento
info = votacao(idade)
print(f'Tem {idade} e é {info} a votação')