n1 = int(input())
cont = 0
n2 = 0 
n3 = 1
print(f'{n2} {n3} ', end='')
cont = 3
while(cont<=n1): 
    
    n4 = n3 +n2
    print(f'{n4} ', end='')
    n2 = n3
    n3 = n4
    
    cont +=1