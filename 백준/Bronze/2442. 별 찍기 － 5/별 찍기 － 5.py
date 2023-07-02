N = int(input())

for i in range(N,0,-1):
    blank = i-1
    star = (2*N)-(2*blank)-1
    print(' '*blank,'*'*star,sep='')
