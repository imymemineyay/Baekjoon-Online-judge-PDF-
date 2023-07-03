N = int(input())

for i in range(0,2*N-1):
    if i <= (N-1):
        star = (2*N-1)-2*i
        blank = i
        print(' '*blank,'*'*star, sep='')
    else: 
        blank = (2*N-1) - i -1
        star = (2*N-1) - blank* 2
        print(' '*blank,'*'*star,sep='')