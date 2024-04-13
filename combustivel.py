i = 0
a = 0
g = 0
d = 0
while i == 0:
    num = int(input())
    if num == 1:
        a = a + 1
    elif num == 2:
        g = g + 1
    elif num == 3:
        d = d + 1
    elif num == 4:
        print('MUITO OBRIGADO')
        print('Alcool:', a)
        print('Gasolina:', g)
        print('Diesel:', d)
        i = 1