n1 = int(input())
for c in range(1,7):
    if(n1%2==0):
        n1 +=1
        print(n1)
        n1 +=2
    elif(not n1%2==0):
        print(n1)
        n1 +=2
    
