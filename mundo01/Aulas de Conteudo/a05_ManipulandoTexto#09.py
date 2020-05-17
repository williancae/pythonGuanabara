'''
Teoria
            frase = 'ola Mundo'
1 - Fatiamento de texto
    1 - frase = 'Ola Mundo'
    2 - é o mesmo de frase = ['O','l','a',' ','M','u','n','d','o']
    3 - frase[4] == ['M'] --> posição dela na lista
    4 - frase[4:7] == ['M','u','n'] --> intervalo de posições tirando a ultima posição informada
    5 - frase[0:9:2] == ['l', ' ', 'u', 'd'] --> intervalo de 0 ao 9 pegando em 2 e 2 posições
    6 - frase[:4] == ['O','l','a'] --> Posição inicial até a informada
    7 - frase[4:] == ['M','u','n','d','o'] --> pega  da posição informada ate o final da lista
    8 - frase[4::3] == ['M','d'] --> inicia no 4, vai ate ao final em 3 e 3
2 - Analise
    1 - frase.len --> conta quantos posições tem a lista
    2 - frase.count('o') --> conta quantas letras informadas tem no lista == 'texto'
    3 - frase.count('o',x,y) --> proucura a letra o no intervalo
    4 - fase.find('Mun') --> procura a informação passada e traz a posição iniciada do elemento na lista
    5 - frase.find('Branco') --> Caso nao exista ele retorna -1
    6 - 'Ola' in frase --> Se existe o elemento informado na lista
3 - Transformação
    1 - frase.replace('Ola', 'Hello') --> substitui um elemento na posição do que foi informado  primeiro
    2 - frase.upper() --> Coloca as letras em MAIUSCULAS
    3 - fase.lower() --> Colocar tudo em minusculo
    4 - frase.capitalize() --> A primeira palavra da frase fica em maiuscula
    5 - frase.title() --> coloca a primeira letra de todas as palavras de uma frase em MAIUSCULO
    6 - frase.strip() --> tira espaço inicias e finais da string matendo o espaçamento do meio
    7 - frase.rstrip() --> frase.'r'strip remove os espaços da direita
    8 - frase.lstrip() --> frase.'l'strip remove espaços da esquerda
    9 - frase.split() --> divisão das palvras em uma frase, gera lista palvras frase = [['Ola'],[' Mundo']]
    10 - '-'.join(frase) --> junsta palvras em uma unica lista
'''
# ============================== Exercicios
frase = 'ola mundo'
print(frase)
print(frase[3])
print(frase[3:6])
print(frase[:6])
print(frase[2:])
print(frase[2:6:2])
print(frase[::2])
print(frase.count('o'))
print(len(frase))
print(frase.replace('ola','hello'))
print('ola' in frase)
print(frase.find('ola'))
print(frase.split())

print("""\n\n\nEiiitaaa Mainhaaa!! Esse Lorem ipsum é só na sacanageeem!! E que abundância meu irmão viuu!! Assim você vai matar o papai. Só digo uma coisa, Domingo ela não vai! Danadaa!! Vem minha odalisca, agora faz essa cobra coral subir!!! Pau que nasce torto, Nunca se endireita. Tchannn!! Tchannn!! Tu du du pááá! Eu gostchu muitchu, heinn! danadinha! Mainhaa! Agora use meu lorem ipsum ordinária!!! Olha o quibeee! rema, rema, ordinária!.""")



