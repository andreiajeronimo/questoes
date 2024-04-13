def display_numbers(numbers):
    for i in range(len(numbers)):
        if i == len(numbers) - 1:  # Check if it's the last number
            print(numbers[i])  # Don't add space after the last number
        else:
            print(numbers[i], end=' ') 

            
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
                    resposta.append(i+1)
            display_numbers(resposta)
    except EOFError:
        break
    