while True:
    tamanho = int(input())

    if tamanho == 0:
        break

    lista = list(map(int, input().split()))

    tem_par = False

    for i in range(0, len(lista)):
        if  lista[i] % 2 == 0:
            tem_par = True

    print('{}'.format(tem_par))