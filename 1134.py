n1 = alcool = gasolina = diesel = 0
while(n1!=4):
    n1  = int(input())
    if(n1==1):
        alcool +=1
    elif(n1==2):
        gasolina +=1
    elif(n1==3):
        diesel +=1
print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')
