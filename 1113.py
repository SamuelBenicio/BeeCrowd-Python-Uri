n1 = 0
n2 = 1
while(n1!=n2):
    n1,n2 = map(int,input().split(' '))
    if(n1>n2):
        print('Decrescente')
    elif(n1<n2):
        print('Crescente')
    elif(n1==n2):
        pass
