n1 = 0
notas = 0
media = 0
while(notas!=2):
    n1 = float(input())
    if(0<n1<=10):
        media +=n1/2
        notas +=1
    else:
        print('nota invalida')
print(f'media = {media}')