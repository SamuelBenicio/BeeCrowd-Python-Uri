n1 = int(input())
musicas = ('PROXYCITY','P.Y.N.G.','DNSUEY!','SERVERS','HOST!','CRIPTONIZE','OFFLINE DAY','SALT','ANSWER!','RAR?','WIFI ANTENNAS')
for c in range(1,n1+1):
    x,y = map(int,input().split())
    z = x+y
    print(musicas[z])
