N = int(input())

for i in range(N):
    star = 2*N-(1+(i*2))
    print(' '*i,'*'*star,sep='')

