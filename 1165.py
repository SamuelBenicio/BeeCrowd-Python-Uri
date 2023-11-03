n1  = int(input())
cont = 0
for c in range(1,n1+1):
    n2 = int(input())
    for p in range(1,n2+1):
        if(n2%p==0):
            cont += 1
    if(cont==2):
        print(f'{n2} eh primo')
    else:
        print(f'{n2} nao eh primo')
    cont = 0
