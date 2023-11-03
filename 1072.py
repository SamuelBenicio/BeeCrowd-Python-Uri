n1 = int(input())
contin = contout = 0
for c in range(1,n1+1):
    x = int(input())
    if(10<=x<=20):
        contin +=1
    else:
        contout +=1
print(f'{contin} in')
print(f'{contout} out')
