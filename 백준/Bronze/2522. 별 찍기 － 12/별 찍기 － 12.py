N = int(input())

for i in range(1,2*N):
    if i <= N:
        print(' '*(N-i),'*'*i, sep='')
    else:
        print(' '*(N-(2*N-i)),'*'*(2*N-i),sep='')
