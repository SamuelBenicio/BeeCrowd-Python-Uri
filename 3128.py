n1 = int(input())
n2 = int(input())
if(n1<6 or n2<6):
    print('NO')
elif(n1<14 and n2>=18):
    print('YES')
elif(n1>=18 and n2<14):
    print('YES')
elif(n1>=14 and n2>=14):
    print('YES')
elif(n1<14 and n2<18):
    print('NO')
elif(n1<18 and n2<14):
    print('NO')
