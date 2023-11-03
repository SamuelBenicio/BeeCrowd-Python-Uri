n1 = contg = conti = empate = cont = 0
while(n1!=2):
    inter,gremio = map(int,input().split(' '))
    print('Novo grenal (1-sim 2-nao)')
    n1 = int(input())
    cont +=1
    if(inter>gremio):
        conti +=1
    elif(gremio>inter):
        contg +=1
    elif(gremio==inter):
        empate +=1
print(f'{cont} grenais')
print(f'Inter:{conti}')
print(f'Gremio:{contg}')
print(f'Empates:{empate}')
if(contg>conti):
    print('Gremio venceu mais')
elif(conti>contg):
    print('Inter venceu mais')
elif(contg==conti):
    print('Nao houve vencedor')
