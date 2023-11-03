n1 = int(input())
totcob = coelhos = ratos =sapos = 0
for c in range(1,n1+1):
    n2,tipo = input().split(' ')
    n2 = int(n2)
    totcob +=n2
    if(tipo=='C'):
        coelhos +=n2
    elif(tipo=='R'):
        ratos +=n2
    elif(tipo=='S'):
        sapos +=n2
print(f'Total: {totcob} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {(coelhos/totcob)*100:.2f} %')
print(f'Percentual de ratos: {(ratos/totcob)*100:.2f} %')
print(f'Percentual de sapos: {(sapos/totcob)*100:.2f} %')
