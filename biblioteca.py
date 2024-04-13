while 1 == 1:
    try:
        n = int(input())
        cod = [0] * n
        for i in range(0,n):
            cod[i] = int(input())
        cod.sort()
        for i in range(0,n):
            if cod[i] < 10 and cod[i] < 100:
                print('000', end='')
            elif cod[i] >= 10 and cod[i] < 100:
                print('00', end='')
            elif cod[i] >= 100 and cod[i] < 1000:
                print('0', end='')
            print(cod[i])
    except EOFError:
        break