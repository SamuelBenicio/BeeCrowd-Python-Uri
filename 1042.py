n1,n2,n3 = map(int,input().split(' '))
lista = [n1,n2,n3]
lista1 = lista[:]
lista.sort()
for c in lista:
    print(c)
print('\n')
for p in lista1:
    print(p)
