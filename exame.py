while 1 == 1:
    try:
        n,q = list(map(int, input().split()))
        nota = [0] * n
        consulta = [0] * q
        for i in range(0, n):
            nota[i] = int(input())
        nota.sort(reverse=True)
        for i in range(0,q):
            consulta[i] = int(input())
        for i in range(0,q):
            print(nota[consulta[i]-1])
    except EOFError:
        break