hi,hf = map(int,input().split(' '))
if(hi>hf):
    print(f'O JOGO DUROU {(hf+24)-hi} HORA(S)')
if(hf>hi):
    print(f'O JOGO DUROU {hf-hi} HORA(S)')
if(hf==hi):
    print('O JOGO DUROU 24 HORA(S)')
