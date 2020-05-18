from datetime import date
anoAtual =  date.today()
anoAtual = int(anoAtual.year)
# -----------------------------
nascimento = int(input('Ano  Nascimento: '))
idade = anoAtual - nascimento

if idade <= 9:
    print('Mirim')
elif  9 <  idade <= 14:
    print('Infantil')
elif 14 < idade <=19:
    print('Junior')
else:
    print('Master')