print(x) #Caso nao seja definida a variavel nameErro

n = int(input('Numero: '))
print(f'Voce digitou: {n}') #caso seja digitado um valor diferente do tipo que foi indicado ValueErro


a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a/b #Divisão por zero ZeroDivisionError
r = a/'b' #Dividir um numero por uma string typeErro 
print('O resultado é {r}')


lst = [2, 6, 4]
print(lst[3])#Caso seja indicado o indice errado indexError 

import uteis # Caso nao exista ModuleNotFoundError

# -------------------------------------------
try:
    # Possiveis problemas que possam acontecer devem ser informados aqui
except ValueError:
    # caso de algum problema informar aqui
    #caso seja digitado um valor diferente do tipo que foi indicado ValueErro
except ZeroDivisionError:
    # caso de algum problema informar aqui
    #Divisão por zero ZeroDivisionError
except IndexError:
    # caso de algum problema informar aqui
    #caso seja digitado um valor diferente do tipo que foi indicado ValueErro
except Exception as erro:
    print(f'O erro  foi {erro.__cause__}')
    # Ira informar o tipo de quaquer erro
else:
    # Caso nao aconteça erro mostre aqui
finally:
    # Mesmo acontecendo um erro o que estiver aqui sera executado  
    #