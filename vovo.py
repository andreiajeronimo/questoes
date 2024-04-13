n,s = list(map(int, input().split()))
saldo = s
b = s
for i in range(0, n):
    a = int(input())
    saldo = saldo + a
    if saldo < b:
        b = saldo
print(b)
