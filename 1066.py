i = 0
par = 0
impar = 0
pos = 0
negativo = 0
while(i!=5):
  i +=1
  n = int(input())
  if(n%2==0):
    par +=1
  if(n%2!=0):
    impar +=1
  if(n>0):
    pos +=1 
  if(n<0):
    negativo +=1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
