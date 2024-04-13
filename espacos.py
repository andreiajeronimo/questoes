num_casos = int(input())

for teste in range(0, num_casos):
    tamanho = int(input())
    lista = list(map(int, input().split()))

    lista.sort(reverse=True) # Ordena a lista em ordem decrescente

    print(lista)