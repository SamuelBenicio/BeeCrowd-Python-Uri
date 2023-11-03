n = 0
cont =0
soma = 0
while(n>=0):
    n = int(input())
    cont +=1
    if(n>0):
        soma +=n
        media = soma/cont
print(f'{media:.2f}')   
