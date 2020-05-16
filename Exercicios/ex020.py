'''
Leia um Angulo e traga o seno, cosseno e tangente
'''
import math
ang = float(input('Digite um Angulo: '))
s = math.sin(ang) #seno do angulo
c = math.cos(ang) #cosseno do angulo
t = math.tan(ang) #tangente do angulo
print('Seno {:.2f}\nCosseno {:.2f}\nTangente {:.2f}'.format(s, c, t))
