
A,B,C = map(float,input().split(' '))
f1 = (B**2)-(4*A*C) #OK
if(A==0) or (f1<0):
    print('Impossivel calcular')
else:
    R1 = (-B+(f1**0.5))/(2*A)
    R2 = (-B-(f1**0.5))/(2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')

