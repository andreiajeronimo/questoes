
p,n = list(map(int, input().split()))
cano = list(map(int, input().split()))
a = 0
 
for i in range(0, n-1):
    if abs(cano[i]-cano[i+1]) > p:
        a = 1
if a == 0:
    print('YOU WIN')
else:
    print('GAME OVER')