N = int(input())
H = N//3600
R = N%3600
M = R//60
S = R%60
print(f'{H}:{M}:{S}')
