n1= 0
while(True):
    try:
        n1=int(input())
        print(n1-1)
    except EOFError:
        break