while 1 == 1:
    try:
        n,r = list(map(int, input().split()))
        vivos = [0] * n
        todos = [0] * n
        vivos = list(map(int, input().split()))
        resposta = []
        if r == n:
            print('*')
        else:
            for i in range(0,r):
                todos[vivos[i]-1] = 1
            for i in range(0, n):
                if todos[i] == 0:
                    print(i+1, end=' ')
            print()
            
    except EOFError:
        break
    