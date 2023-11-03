n1,n2,n3 = map(int,input().split(' '))
if(n1>n2 and n1>n3):
    print(f'{n1} eh o maior')
elif(n2>n1 and n2>n3):
    print(f'{n2} eh o maior')
elif(n3>n1 and n3>n2):
    print(f'{n3} eh o maior')
