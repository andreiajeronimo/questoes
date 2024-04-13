n = int(input())
resposta = []
for i in range(0,n):
    m = int(input())
    notas = [0] * m
    aux = [0] * m
    x = 0
    notas = list(map(int, input().split()))
    for i in range(0,m):
        aux[i] = notas[i]
    notas.sort(reverse=True)
    for i in range(0,m):
        if notas[i] == aux[i]:
            x = x + 1
    resposta.append(x)
for i in range(0,n):
    print(resposta[i])