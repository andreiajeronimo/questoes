m = int(input())
a = int(input())
b = int(input())
c = m - (a+b)

if a > b:
    if a > c:
        print(a)
    elif a == c:
        print(a)
    else:
        print(c)
elif a < b:
    if b > c:
        print(b)
    elif b == c:
        print(b)
    else:
        print(c)
else:
    print(a)