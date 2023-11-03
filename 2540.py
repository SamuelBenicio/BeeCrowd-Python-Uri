
while(True):
    try:
        n1 = int(input())
        votos = input().split()
        votos = votos.count('1')
        if(votos/n1) >= 2/3:
            print('impeachment')
        else:
            print('acusacao arquivada')
    except EOFError:
        break        
