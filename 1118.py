media = 0
notas = 0
novo = 0
while(notas!=2):
    n1 = float(input())
    if(0<=n1<=10):
        media +=n1/2
        notas +=1
        if(notas==2):
            print(f'media = {media:.2f}')
            print('novo calculo (1-sim 2-nao)')
            novo = int(input())
            while(novo!=1 and novo!=2):
                print('novo calculo (1-sim 2-nao)')
                novo = int(input())
            if(novo==1):
                notas = 0
                media = 0
    else:
        print('nota invalida')