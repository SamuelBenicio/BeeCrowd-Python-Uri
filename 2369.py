n = int(input())
if(0<=n<=10):
    print(7)
elif(11<=n<=30):
    print((7)+(n-10))
elif(31<=n<=100):
    print((7)+(20)+((n-31)*2)+2)
elif(n>=101):
    print((7)+(20)+(140)+((n-101)*5)+5)