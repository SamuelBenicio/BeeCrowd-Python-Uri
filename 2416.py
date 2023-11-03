n1,n2 = map(int,input().split(' '))
if(1<=n1 and n1<=10**8) and (1<=n2 and n2<=100):
    print(f'{n1%n2}')