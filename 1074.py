n = int(input())
for c in range(1,n+1):
    x = int(input())
    if(x%2==0 and x>0):
        print('EVEN POSITIVE')
    elif(not x%2==0 and x>0):
        print('ODD POSITIVE')
    elif(x==0):
        print('NULL')
    elif(x%2==0 and x<0):
        print('EVEN NEGATIVE')
    elif(not x%2==0 and x<0):
        print('ODD NEGATIVE')