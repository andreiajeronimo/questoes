p = int(input())
d_1 = int(input())
d_2 = int(input())
dedo = (d_1+d_2)%2
if dedo == 0:
    if p == 0:
        print('0')
    else:
        print('1')
else:
    if p == 0:
        print('1')
    else:
        print('0')