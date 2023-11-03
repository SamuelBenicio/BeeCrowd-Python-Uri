while(True):
    try:
        n1 = int(input())
        cont = menor =0
        for c in range(1,n1+1):
            n2 = float(input())
            cont +=1
            if(cont==1):
                menor = n2
            else:
                if(n2<menor):
                    menor = n2
        print(menor)
    except EOFError:
        break
