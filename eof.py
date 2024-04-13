while 1 == 1:
    try:
        a = int(input())

        print('X = {}'.format(a % 2 == 0))
    except EOFError:
        break