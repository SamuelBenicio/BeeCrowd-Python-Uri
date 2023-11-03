n1 =n2=1
while(n1!=0 and n2!=0):
    n1,n2 = map(int,input().split(' '))
    if(n1==0 or n2==0):
        break
    soma = 0
    for i in range(n2,n1+1):
        print(i,end=' ')
        soma +=i
        if(i==n1):
            print(f'Sum={soma}',end='\n')
    
