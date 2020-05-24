n = int(input('Digite numero: '))
r = int(input('Razão: '))
t = (n + (10 - 1) * r) + r
x = 0
while x != t:
    print(x, end=' >> ')
    x += r
    # if x == t:
        # a = int(input('Quer continuar S[1] ou N[0]'))
        # if a == 1:
        #     n = int(input('Digite numero: '))
        #     r = int(input('Razão: '))
        #     t = (n + (10 - 1) * r) + r
        #     x += r
print('Fim')