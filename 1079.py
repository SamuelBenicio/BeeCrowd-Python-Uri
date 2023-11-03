n = int(input())
for c in range(1,n+1):
    n1,n2,n3 = map(float,input().split(' '))
    print(f'{((n1*2)+(n2*3)+(n3*5))/10:.1f}')