n = float(input())
if(0<=n<=2000):
    print('Isento')
elif(2000.01<=n<=3000):
    print(f'R$ {(n-2000)*0.08:.2f}')
elif(3000.01<=n<=4500):
    print(f'R$ {(1000*0.08)+((n-3000)*0.18):.2f}')
else:
    print(f'R$ {(1000*0.08)+(1500*0.18)+((n-4500)*0.28):.2f}')
