cmaior = maior = 0
for c in range(1,101):
    n1 = int(input())
    if(c==1):
        maior = n1
        cmaior = c
    else:
        if(n1>maior):
            maior = n1
            cmaior = c
print(maior)
print(cmaior)
