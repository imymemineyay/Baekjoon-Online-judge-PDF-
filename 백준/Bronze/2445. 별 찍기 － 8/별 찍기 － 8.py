N = int(input())

for i in range(1,2*N):
    if i <= (2*N//2):
        print('*'*i,' '*(2*N-2*i),'*'*i,sep='')
    else:
        star = 2*N - i
        blank = 2*N- (2*N - i)*2
        print('*'*star,' '*blank,'*'*star,sep='')