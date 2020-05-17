# Operadores Aritmeticos
'''
==================
Operadores
+ Adição
- Subtração
/ Divisão
* Multiplicação
** Potencia
% Resto da Divisão
// Divsão inteira
====================
Ordem de precedencia
1° ()
2° **
3° * / % //
4° + -

'''

# Funcionalidades

nome = input("Digite seu nome: ")
i = 1.34967654345654345
print('='*30)
print('Prazer {:20}!='.format(nome)) #{:20} --> 20 espaços depois do 'nome'
print('Prazer {:>20}!='.format(nome)) #{:>20} --> alinha o 'nome' a direita em 20 espaçoes
print('Prazer {:<20}!='.format(nome)) #{:<20} --> Alinhado a esquerda e 20 espaço após
print('Prazer {:^20}!='.format(nome)) #{:^20} --> alinha ao centro entre os 20 espaços
print('Prazer {:-^20}=!'.format(nome)) #{:-^20} --> alinha ao centro entre os 20 traços
print('Prazer {:->20}=!'.format(nome)) #{:->20} --> alinha a direita depois de 20 traços
print('Prazer {:-<20}=!'.format(nome)) #{:-<20} --> alinha a esquerda com traços 20 traços depois
print("="*30)
print('Formatação de Numeros')
print('O numero é: {:.2f}'.format(i),end='')# (end='') Faz com que nao quebre a linha no proximo print
print('!')
