x = float(input())
if(0<=x<=400):
    print(f'Novo salario: {x*1.15:.2f}')
    print(f'Reajuste ganho: {(x*1.15)-x:.2f}')
    print('Em percentual: 15%')
elif(400.01<=x<=800):
    print(f'Novo salario: {x*1.12:.2f}')
    print(f'Reajuste ganho: {(x*1.12)-x:.2f}')
    print('Em percentual: 12%')
elif(800.01<=x<=1200):
    print(f'Novo salario: {x*1.1:.2f}')
    print(f'Reajuste ganho: {(x*1.1)-x:.2f}')
    print('Em percentual: 10%')
elif(1200.01<=x<=2000):
    print(f'Novo salario: {x*1.07:.2f}')
    print(f'Reajuste ganho: {(x*1.07)-x:.2f}')
    print('Em percentual: 7%')
else:
    print(f'Novo salario: {x*1.04:.2f}')
    print(f'Reajuste ganho: {(x*1.04)-x:.2f}')
    print('Em percentual: 4%')
