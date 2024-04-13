x = int(input())
z = int(input())
valor = 0
i = 0
while z <= x:
    z = int(input())
while valor < z:
    valor = x + valor
    x = x + 1
    i = i + 1
print(i)