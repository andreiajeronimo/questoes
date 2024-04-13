a = int(input())
b = int(input())
c = int(input())
h = int(input())
l = int(input())

if a > h:
    if b > h:
        if c > h:
            print('N')
        else:
            if a <= l or b <= l:
                print('S')
            else:
                print('N')
    else:
        if a <= l or c <= l:
            print('S')
        else:
            print('N')
else:
    if b <= l or c <= l:
        print('S')
    else:
        print('N')