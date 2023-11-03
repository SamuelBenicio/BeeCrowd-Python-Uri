n = 0
pos = 0
soma = 0
media = 0
while(n!=6):
    x = float(input())
    n +=1
    if(x>0):
        pos +=1
        soma +=x
        media = soma/pos
print(f'{pos} valores positivos')
print(f'{media:.1f}')
