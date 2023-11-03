n1,n2,n3,n4 = map(float,input().split(' ')) #1 casa de decimal :.1f
n1 = n1*2 
n2 = n2*3
n3 = n3*4
m = (n1+n2+n3+n4)/(2+3+4+1)
print(f'Media: {m:.1f}')
if(m>=7.0):
    print('Aluno aprovado.')
elif(m<5.0):
    print('Aluno reprovado.')
elif(5.0<=m<=6.9):
    print('Aluno em exame.')
    ex = float(input())
    m2 = (ex+m)/2
    print(f'Nota do exame: {ex:.1f}')
    if(m2>=5.0):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {m2:.1f}')
