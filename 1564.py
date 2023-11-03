while(True):
    try:
        n1 = int(input())
        if(n1==0):
            print('vai ter copa!')
        if(n1>0):
            print('vai ter duas!')
    except EOFError:
        break
    